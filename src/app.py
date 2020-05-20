import tweepy
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def callback():
    return render_template("hello.html", greet="Hello, Flask!")


if __name__ == "__main__":
    app.run(debug=True)
