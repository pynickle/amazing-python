
# -*- coding: utf-8 -*-
import difflib
import hashlib
import os
import threading
import queue

from flask import Flask, render_template, request, flash, redirect,\
    get_flashed_messages, session, jsonify, url_for,\
    send_from_directory, current_app, g
from flask_sqlalchemy import SQLAlchemy
from flask_github import GitHub
from werkzeug import secure_filename
import requests
from dotenv import find_dotenv,load_dotenv

import traceback

from src import SpiderForm, youdict, hujiang, words_validate, mail

load_dotenv(find_dotenv())

def youdict_spider(threadName, q):
    """
    :param threadName: thread name of threading module
    :param q: Queue object of queue

    Usage::

        get youdict words and store them in the sqlalchemy database
    """
    words = youdict(threadName, q)
    for i in words:
        word = Words(i[0], i[1])
        try:
            db.session.add(word)
            db.session.commit()
        except BaseException:
            pass


def hujiang_spider(threadName, q):
    """
    :param threadName: thread name of threading module
    :param q: Queue object of queue module
    
    Usage::

        get hujiang words and store them in the sqlalchemy database
    """
    words = hujiang(threadName, q)
    for i in words:
        word = Words(i[0], i[1])
        db.session.add(word)
        db.session.commit()


class SpiderThread(threading.Thread):
    """
    :param name: thread name
    :param q: queue object of queue module
    :param website: the words website to scrapy

    :method run:

        run the words scrapy program with threading and queue
    """
    def __init__(self, name, q, website):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.website = website

    def run(self):
        print("Starting " + self.name)
        while True:
            try:
                if self.website == "youdict":
                    youdict_spider(self.name, self.q)
                elif self.website == "hujiang":
                    hujiang_spider(self.name, self.q)
            except BaseException:
                break
        print("Exiting" + self.name)


app = Flask(__name__)
app.jinja_env.auto_reload = True

app.config.from_object("config")
db = SQLAlchemy(app)
github = GitHub(app)


class Words(db.Model):
    """
    :attr|param id: id for words
    :attr|param english: english for words
    :attr|param chinese: chinese explanation for english words
    """
    id = db.Column("words_id", db.Integer, primary_key=True)
    english = db.Column(db.String(75))
    chinese = db.Column(db.String(200))

    def __init__(self, english, chinese):
        self.english = english
        self.chinese = chinese


class WrongWords(db.Model):
    """
    :attr|param id: id for 1wrong words
    :attr|param english: english for wrong words
    :attr|param chinese: chinese explanation for english wrong words
    """
    __bind_key__ = "wrongwords"
    id = db.Column("wrong_words_id", db.Integer, primary_key=True)
    english = db.Column(db.String(75))
    chinese = db.Column(db.String(200))

    def __init__(self, english, chinese):
        self.english = english
        self.chinese = chinese

class GithubUsers(db.Model):
    """
    :attr|param id: id for users
    :attr|param username: username of github
    """
    __bind_key__ = "github-users"
    id = db.Column("github-users_id", db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    access_token = db.Column(db.String(200))

    def __init__(self, username, access_token):
        self.username = username
        self.access_token = access_token

class AdminUsers(db.Model):
    """
    :attr|param id: id for users
    :attr|param username: username of github
    """
    __bind_key__ = "admin-users"
    id = db.Column("admin-users_id", db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.before_first_request
def before_first_request():
    """
    Usage::

        Before first request for the application, we need to
        initialize some variables.
    """
    global choice, failure, is_failure, first, wrong_word_choice
    global db

    choice = 0
    failure = []
    is_failure = False
    first = True
    wrong_word_choice=0

    session.permanent = True
    session["search_diff"] = 0.5
    session["words_count"] = 20
    session["recite_progress"] = 0

    db.create_all()
    db.create_all(bind="wrongwords")
    db.create_all(bind="github-users")
    db.create_all(bind="admin-users")

@app.before_request
def before_request():
    g.user = None
    if 'users_id' in session:
        g.user = GithubUsers.query.get(session['users_id'])
    elif 'admin_users_id' in session:
        g.user = AdminUsers.query.get(session["admin_users_id"])

@app.route("/")
def main():
    """
    Usage::

        the index page for cishen application
    """
    if g.user:
        is_login = "true"
        if isinstance(g.user, GithubUsers):
            response = github.get('user')
            username = response['name']
        elif isinstance(g.user, AdminUsers):
            username = g.user.username
        return render_template('main.html', is_login=is_login, username=username)
    is_login = "false"
    return render_template("main.html", is_login = is_login)

@app.route("/registe")
def registe():
    return render_template("registe/registe.html")

@app.route("/registe/normal", methods=["POST"])
def registe_normal():
    md5 = hashlib.md5()
    registe_username = request.form.get("username")
    registe_password = request.form.get("password")
    md5.update(registe_password.encode(encoding="utf-8"))
    registe_password = md5.hexdigest()
    if AdminUsers.query.filter_by(username=registe_username, password=registe_password).first() is not None:
        flash("用户名已存在！")
        return redirect("/registe")
    user = AdminUsers(registe_username, registe_password)
    db.session.add(user)
    db.session.commit()
    flash("注册成功")
    return redirect("/")

@app.route("/login")
def login():
    return render_template("login/login.html")

@app.route("/login/normal", methods=["POST"])
def login_normal():
    md5 = hashlib.md5()
    login_username = request.form.get("username")
    login_password = request.form.get("password")
    md5.update(login_password.encode(encoding="utf-8"))
    login_password = md5.hexdigest()
    user = AdminUsers.query.filter_by(username = login_username, password = login_password).first()
    if user:
        password = user.password
        if password == login_password:
            flash("登录成功！")
            session["admin_users_id"] = user.id
            return redirect("/")
        else:
            flash("用户名或密码错误！")
    else:
        flash("用户名或密码错误！")

@app.route('/login/oauth2')
def login_oauth2():
    if session.get('users_id', None) is None:
        return github.authorize()
    flash('已经登录！')
    return redirect("/")

@app.route('/login/oauth2/callback')
@github.authorized_handler
def oauth2_callback(access_token):
    if access_token is None:
        flash('登陆失败！')
        return redirect("/")

    response = github.get('user', access_token=access_token)
    username = response['login']  # get username
    user = GithubUsers.query.filter_by(username=username).first()
    if user is None:
        user = GithubUsers(username=username, access_token=access_token)
        db.session.add(user)
    db.session.commit()
    session["users_id"] = user.id
    flash('登录成功！')
    return redirect("/")

@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.access_token

@app.route("/see-words", methods=["GET", "POST"])
def see_words_redirect():
    return redirect("/see-words/1")

@app.route("/see-words/<page>", methods=["GET", "POST"])
def see(page):
    """
    Usage::

        The page for seeing all words in the databases. It can delete
        some words or all words.
    """
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
            return render_template("see-words/see.html",
                                   words=Words.query.all())
    else:
        info = Words.query.paginate(int(page), per_page = 30)
        return render_template("see-words/see.html", words=info)


@app.route("/add-new-word", methods=["GET", "POST"])
def new():
    """
    Usage::

        the page for href to use hand or file to add new words. Also accept
        post from hand page.
    """
    if request.method == "GET":
        return render_template("add-new-word/new.html")
    else:
        success, errors = words_validate(request.form.get("words"))
        for data in success:
            word = Words(data[0], data[1])
            db.session.add(word)
        db.session.commit()
        return redirect("see-words")


@app.route("/recite-words")
def recite():
    """
    Usage::

        The page for recite words in the words database. Accept the first
        get and other post for data transmission.
    """
    global first, choice, failure

    # get all words
    words = []
    for i in Words.query.all():
        words.append([i.english, i.chinese])

    if not words:
        flash("请先添加单词！")
        return redirect("/")

    #get recite progress to start from here
    recite_progress = session.get("recite_progress")
    if not recite_progress:
        recite_progress = "0"
    else:
        recite_progress = str(recite_progress)

    # get other args from url
    choice = request.args.get("choice")
    input_data = request.args.get("input")
    data = request.args.get("data")
    wrong = request.args.get("wrong")

    # if you answered wrong, it will add the word to the wrong words database
    if wrong == "True":
        wrongword = words[int(choice)-1]
        failure.append([wrongword[0], wrongword[1]])
        wrongword = WrongWords(wrongword[0], wrongword[1])
        db.session.add(wrongword)
        db.session.commit()

    choice = int(choice)

    # judge if we have finished the recite
    if choice >= int(recite_progress) + session.get("words_count") or choice >= len(words):
        session["recite_progress"] = choice
        if failure:
            return redirect("/recite-wrong-words?choice=0")
        else:
            flash("复习完成！")
            return redirect("/")
    word = words[choice]

    # other situations
    if input_data and data:
        return redirect("/recite-words")
    elif choice != None:
        return render_template("/recite-words/recite.html", word=word)

@app.route("/recite-wrong-words")
def recite_words_wrong():
    global failure

    # get args from url
    wrong_word_choice = int(request.args.get("choice"))
    input_data = request.args.get("input")
    data = request.args.get("data")
    wrong = request.args.get("wrong")

    # judge if you answered right, if right, remove the word from failure list
    if not wrong:
        pass
    elif wrong == "False":
        failure.remove(failure[wrong_word_choice-1])
    else:
        failure.append(failure[wrong_word_choice-1])

    # when failure is empty, it means you finished recite
    if not failure:
        flash("复习完成！")
        return redirect("/")

    # other situations
    if input_data and data:
        return redirect("/recite-wrong-words")
    elif choice != None:
        return render_template("/recite-words/recite.html", word=failure[wrong_word_choice], come="wrong")

@app.route("/search-words", methods=["GET", "POST"])
def search():
    """
    Usage::

        The page for search words from words database. Accept get and post of 
        key word for search.
    """
    if request.method == "GET":
        return render_template("search-words/search.html")
    else:
        result = []
        data = request.form.get("data")
        for i in Words.query.all():
            sm = difflib.SequenceMatcher(None, i.english, data)
            search_diff = session.get("search_diff")
            search_diff = 0.5 if not search_diff else search_diff
            if sm.ratio() >= search_diff:
                result.append(i)
        return render_template("search-words/result.html", result=result)


@app.route("/wrong-words", methods=["GET", "POST"])
def wrong_words():
    """
    Usage::

        The page for show wrong words from wrongwords database. Accept get
        and post for deleting.
    """
    if request.method == "POST":
        delete_all = request.form.get("delete-all")
        if delete_all:
            words = WrongWords.query.all()
            for i in words:
                db.session.delete(i)
            db.session.commit()
            return redirect("/wrong-words")
        else:
            english = request.form.get("english")
            chinese = request.form.get("chinese")
            u = WrongWords.query.filter_by(
                english=english, chinese=chinese).first()
            db.session.delete(u)
            db.session.commit()
            return render_template(
                "wrong-words/wrong.html", words=WrongWords.query.all())
    else:
        return render_template("wrong-words/wrong.html",
                               words=WrongWords.query.all())


@app.route("/settings", methods=["GET", "POST"])
def settings():
    """
    Usage::

        The settings page. Settings contains the words count you want to recite
        one time, the scrapy program for two websites.
    """
    youdictform = SpiderForm()
    hujiangform = SpiderForm()
    if request.method == "GET":
        return render_template("/settings/settings.html", words_count=session.get("words_count"),
                               search_diff=session.get("search_diff"),
                               youdictform=youdictform, hujiangform=hujiangform)
    else:
        search_diff = request.form.get("search_diff")
        words_count = request.form.get("words_count")
        try:
            search_diff = float(search_diff)
            words_count = int(words_count)
        except Exception:
            flash("数值不合法")
            return redirect("/settings")
        if search_diff>1 or search_diff<0:
            flash("查询单词相似度数值不合法！")
            return redirect("/settings")
        if words_count<=0 or words_count%1 != 0:
            flash("每次背诵单词数数值不合法！")
            return redirect("/settings")
        session["search_diff"] = search_diff
        session["words_count"] = words_count
        flash("修改设置成功")
        return render_template("/settings/settings.html", words_count=session.get("words_count"),
                               search_diff=session.get("search_diff"),
                               youdictform=youdictform, hujiangform=hujiangform)


@app.route("/spider/<website>", methods=["POST"])
def youdict_spider_post(website):
    """
    :param website: the website name to scrapy

    Usage::

        The page for scrapy website operation. Accept post
        with website name.
    """
    # print(website)
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
    # print(link_list)

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


@app.route("/word-books")
def word_books():
    """
    Usage::

        The word books page. The word books is used for
        download the prepared words. It is faster than scrapy.
    """
    return render_template("word-books/books.html")


@app.route("/word-books/download/<name>", methods=["POST"])
def word_books_download(name):
    """
    :param name: the name of the word book

    Usage::

        The word books download page for only post method. Word books can be
        download here and added to the words databases.
    """
    file = "./static/word-books/" + name + ".txt"
    f = open(file, "r", encoding="utf-8").read()
    url = url_for("new", _external=True)
    requests.post(url, data={"words": f})
    return redirect("/see-words")


@app.route("/add-new-word/hand")
def hand():
    """
    Usage::

        The page for add new word by hand. Have a post for add new word
        index page to transmit word data.
    """
    return render_template("add-new-word/hand.html")


@app.route("/add-new-word/file", methods=["GET", "POST"])
def file():
    if request.method == "POST":
        try:
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(filename)
            with open(filename, "r", encoding="utf-8") as f:
                success, errors = words_validate(f.read())
            os.remove(filename)
            for data in success:
                word = Words(data[0], data[1], data[2])
                db.session.add(word)
            db.session.commit()
            os.remove(filename)
            return render_template("see-words/see.html",
                                   words=Words.query.all())

        except UnicodeDecodeError:
            return render_template(
                "add-new-word/failure1.html", filename=filename)
        except Exception:
            return render_template(
                "add-new-word/failure2.html", filename=filename)
    else:
        return render_template("add-new-word/file.html")


@app.errorhandler(404)
def four_zero_four(exception):
    """
    Usage::

        The 404 page for this flask application.
    """
    return render_template("error-handler/404.html", exception=exception)


@app.errorhandler(500)
def five_zero_zero(exception):
    """
    Usage::

        The 500 page for this flask application.
    """
    mail(exception)
    return render_template("error-handler/500.html")


@app.route('/favicon.ico')
def favicon():
    """
    Usage::

        The favicon for every page.
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(port=8080, debug = True)
