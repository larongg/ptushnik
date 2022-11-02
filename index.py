from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/add-post")
def add_post():
    return render_template("add-post.html")


@app.route("/posts", methods=["POST", "GET"])
def posts():
    if request.method == "POST":
        searchRequest = request.form['searchRequest']
        return searchRequest
    else:
        return "homo"


if __name__ == "__main__":
    app.run(debug=True)
