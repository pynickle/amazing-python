from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = 'development key'


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/add-new-word")
def new():
    return render_template("add-new-word/new.html")

@app.route("/recite-words")
def recite():
    return render_template("recite-words/recite.html")

@app.route("/search-words")
def search():
    return render_template("search-words/search.html")

@app.route("/add-new-word/hand")
def hand():
    return render_template("")

if __name__ == '__main__':
    app.run(debug=True)
