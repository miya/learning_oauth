import os
import tweepy
from flask import Flask, render_template

app = Flask(__name__)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")


@app.route("/")
def callback():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    redirect_url = auth.get_authorization_url()
    return render_template("hello.html", redirect_url=redirect_url)


if __name__ == "__main__":
    app.run(debug=True)
