from datetime import timedelta
import difflib
import os

from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import threading
import queue

from forms import HandForm, SpiderForm
from validate import words_validate
from spider import youdict, hujiang


def youdict_spider(threadName, q):
    words = youdict(threadName, q)
    for i in words:
        word = Words(i[0], i[1])
        db.session.add(word)
        db.session.commit()

def hujiang_spider(threadName, q):
    words = hujiang(threadName, q)
    for i in words:
        word = Words(i[0], i[1])
        db.session.add(word)
        db.session.commit()

class SpiderThread(threading.Thread):
    def __init__(self, name, q, website):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.website = website
    # run
    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                if self.website == "youdict":
                    youdict_spider(self.name, self.q)
                elif self.website == "hujiang":
                    hujiang_spider(self.name, self.q)
            except:
                break
        print("Exiting" + self.name)


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.jinja_env.auto_reload = True
app.config["DEBUG"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)


@app.before_first_request
def before_first_request():
    global choice, failure, is_failure
    choice = 0
    failure = []
    is_failure = False


db = SQLAlchemy(app)


class Words(db.Model):
    id = db.Column("words_id", db.Integer, primary_key=True)
    english = db.Column(db.String(30))
    chinese = db.Column(db.String(75))

    def __init__(self, english, chinese):
        self.english = english
        self.chinese = chinese


db.create_all()


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/see-words", methods=["GET", "POST"])
def see():
    if request.method == "POST":
        delete_all = request.form.get("delete-all")
        print(delete_all)
        if delete_all:
            words = Words.query.all()
            for i in words:
                db.session.delete(i)
            db.session.commit()
            return redirect("/see-words")
        else:
            english = request.form.get("english")
            chinese = request.form.get("chinese")
            u = Words.query.filter_by(english=english, chinese=chinese).first()
            db.session.delete(u)
            db.session.commit()
            return render_template("see-words/see.html", words=Words.query.all())
    else:
        return render_template("see-words/see.html", words=Words.query.all())


@app.route("/add-new-word", methods=["GET", "POST"])
def new():
    form = HandForm()
    if request.method == "GET":
        return render_template("add-new-word/new.html")
    else:
        success, errors = words_validate(form.words.data)
        for data in success:
            word = Words(data[0], data[1])
            db.session.add(word)
        db.session.commit()
        return redirect("see-words")


@app.route("/recite-words", methods=["GET", "POST"])
def recite():
    global choice, failure, is_failure
    if request.method == "GET":
        words = []
        for i in Words.query.all():
            words.append(i)
        if words:
            return render_template("recite-words/recite.html", words=words, choice=choice, failure=False)
        else:
            flash("请先添加单词！")
            return redirect("/")
    else:
        words = []
        for i in Words.query.all():
            words.append(i)
        data = request.form.get("data")
        form_failure = request.form.get("is-failure")
        word = words[choice]
        if is_failure:
            is_failure = True
            word = failure[choice]
        if data:
            if data == word.english:
                if form_failure:
                    failure.remove(word)
                return render_template("recite-words/result.html", data=data, word=word, status="答对咯！", failure=is_failure)
            else:
                failure.append(word)
                return render_template("recite-words/result.html", data=data, word=word, status="答错了！", failure=is_failure)
        else:
            if form_failure:
                is_failure = True
                word = failure[choice]
                failure.remove(word)
                if not failure:
                    print("2")
                    is_failure = False
                    failure = []
                    flash("复习完成！")
                    return redirect("/")
            choice += 1
            words_count = 20 if not session.get(
                "words_count") else session.get("words_count")
            lst_choice = words_count if not is_failure else len(failure)
            if choice >= len(words) or choice >= lst_choice:
                choice = 0
                if not failure:
                    print("3")
                    is_failure = False
                    failure = []
                    flash("复习完成！")
                    return redirect("/")
                else:
                    is_failure = True
                    return render_template("recite-words/recite.html", words=failure, choice=choice, failure=True)
            return render_template("recite-words/recite.html", words=words, choice=choice)


@app.route("/search-words", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search-words/search.html")
    else:
        result = []
        data = request.form.get("data")
        for i in Words.query.all():
            sm = difflib.SequenceMatcher(None, i.english, data)
            if sm.ratio() >= 0.5:
                result.append(i)
        return render_template("search-words/result.html", result=result)


@app.route("/settings", methods=["GET", "POST"])
def settings():
    youdictform = SpiderForm()
    hujiangform = SpiderForm()
    if request.method == "GET":
        return render_template("settings/settings.html", words_count=session.get("words_count"), 
        youdictform = youdictform, hujiangform = hujiangform)
    else:
        session["words_count"] = int(request.form.get("words_count"))
        flash("修改设置成功")
        return render_template("/settings/settings.html", words_count=session.get("words_count"), 
        youdictform = youdictform, hujiangform = hujiangform)

@app.route("/spider/<website>", methods = ["POST"])
def youdict_spider_post(website):
    print(website)
    youdictform = SpiderForm()
    hujiangform = SpiderForm()
    link_list = []
    if website == "youdict":
        page_number_begin = youdictform.page_number_begin.data
        page_number_all = youdictform.page_number_all.data

        finish = page_number_begin + page_number_all
    elif website == "hujiang":
        page_number_begin = hujiangform.page_number_begin.data
        page_number_all = hujiangform.page_number_all.data

        finish = page_number_begin + page_number_all

    if finish > 2239 or finish < 0 or finish % 1 != 0:
        flash("非法的页数")
        return redirect("/settings")

    for i in range(page_number_begin, finish):
        if website == "youdict":
            url = f"https://www.youdict.com/ciku/id_0_0_0_0_{i}.html"
        elif website == "hujiang":
            url = f"https://www.hujiang.com/ciku/zuixinyingyudanci_{i}"
        link_list.append(url)
    print(link_list)

    threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]
    workQueue = queue.Queue(2500)
    threads = []

    for tName in threadList:
        thread = SpiderThread(tName, workQueue, website)
        thread.start()
        threads.append(thread)

    for url in link_list:
        workQueue.put(url)

    for t in threads:
        t.join()
    
    return redirect("/see-words")

@app.route("/add-new-word/hand")
def hand():
    form = HandForm()
    return render_template("add-new-word/hand.html", form=form)


@app.route("/add-new-word/file", methods=["GET", "POST"])
def file():
    if request.method == "POST":
        try:
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(filename)
            with open(filename, "r", encoding="utf-8") as f:
                success, errors = words_validate(f.read())
            for data in success:
                word = Words(data[0], data[1], data[2])
                db.session.add(word)
            db.session.commit()
            os.remove(filename)
            return render_template("see-words/see.html", words=Words.query.all())

        except UnicodeDecodeError:
            return render_template("add-new-word/failure1.html", filename=filename)
        except Exception:
            return render_template("add-new-word/failure2.html", filename=filename)
    else:
        return render_template("add-new-word/file.html")


@app.errorhandler(404)
def four_zero_four(exception):
    return render_template("404.html", exception=exception)


if __name__ == '__main__':
    app.run(port=8080)
