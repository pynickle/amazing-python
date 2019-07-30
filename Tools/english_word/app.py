from datetime import timedelta
import difflib

from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from forms import HandForm
from validate import words_validate
from werkzeug import secure_filename


app = Flask(__name__)
app.secret_key = "key"
app.jinja_env.auto_reload = True
app.config["DEBUG"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds = 1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.sqlite3'

choice = 0


db = SQLAlchemy(app)
class Words(db.Model):
    id = db.Column("words_id", db.Integer, primary_key = True)
    english = db.Column(db.String(30))  
    part_speech = db.Column(db.String(15))
    chinese = db.Column(db.String(75))

    def __init__(self, english, part_speech, chinese):
        self.english = english
        self.part_speech = part_speech 
        self.chinese = chinese

db.create_all()

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/see-words", methods = ["GET", "POST"])
def see():
    if request.method == "POST":
        english = request.form.get("english")
        chinese = request.form.get("chinese")
        part_speech = request.form.get("part_speech")
        u = Words.query.filter_by(english=english, chinese=chinese, part_speech=part_speech).first() 
        db.session.delete(u)
        db.session.commit()
        return render_template("see-words/see.html", words = Words.query.all())
    else:
        return render_template("see-words/see.html", words = Words.query.all())

@app.route("/add-new-word", methods=["GET", "POST"])
def new():
    form = HandForm()
    if request.method == "GET":
        return render_template("add-new-word/new.html")
    else:
        success, errors = words_validate(form.words.data)
        for data in success:
            word = Words(data[0], data[1], data[2])
            db.session.add(word)
        db.session.commit()
        return redirect("see-words")

@app.route("/recite-words", methods = ["GET", "POST"])
def recite():
    global choice
    if request.method == "GET":
        words = []
        for i in Words.query.all():
            words.append(i)
        return render_template("recite-words/recite.html", words = words, choice = choice)
    else:
        words = []
        for i in Words.query.all():
            words.append(i)
        data = request.form.get("data")
        if data:
            if data == words[choice].english:
                return render_template("recite-words/result.html", data = data, word = words[choice], status="答对咯！")
            else:
                return render_template("recite-words/result.html", data = data, word = words[choice], status="答错了！")
        else:
            choice += 1
            if choice >= len(words):
                choice = 0
                return redirect("/")
            return render_template("recite-words/recite.html", words = words, choice = choice)

@app.route("/search-words", methods = ["GET", "POST"])
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

@app.route("/add-new-word/hand")
def hand():
    form = HandForm()
    return render_template("add-new-word/hand.html", form=form)

@app.route("/add-new-word/file", methods = ["GET", "POST"])
def file():
    if request.method == "POST":
        try:
            f = request.files['file']
            filename = f.filename
            f.save(filename)
            with open(filename, "r", encoding="utf-8") as f:
                success, errors = words_validate(f.read())
            for data in success:
                word = Words(data[0], data[1], data[2])
                db.session.add(word)
            db.session.commit()
            return render_template("see-words/see.html", words = Words.query.all())
            
        except UnicodeDecodeError:
            return render_template("add-new-word/failure1.html", filename=filename)
        except Exception:
            return render_template("add-new-word/failure2.html", filename=filename)
    else:
        return render_template("add-new-word/file.html")

@app.errorhandler(404)
def four_zero_four(exception):
    return render_template("404.html", exception = exception)

if __name__ == '__main__':
    app.run()
