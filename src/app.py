import os
import tweepy
from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = "hogehoge"

callback_url = "http://127.0.0.1:5000/callback"

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")


@app.route("/")
def twitter_auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback_url)

    # 認証用のリダイレクトURLを生成、htmlに表示させる
    try:
        redirect_url = auth.get_authorization_url()
        return render_template("hello.html", redirect_url=redirect_url)
    except tweepy.TweepError:
        return render_template("error.html")


@app.route("/callback")
def callback():
    token = request.values.get("oauth_token", None)
    verifier = request.values.get("oauth_verifier", None)

    if token is None or verifier is None:
        return False

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.request_token = {
        "oauth_token": token,
        "oauth_token_secret": verifier
    }

    auth.get_access_token(verifier)
    auth.set_access_token(auth.access_token, auth.access_token_secret)

    api = tweepy.API(auth)
    user = get_user_data(api)

    return render_template("result.html", user=user)


def get_user_data(api):
    user = api.me()
    return {
        "name": user.name,
        "screen_name": user.screen_name,
        "id_str": user.id_str,
        "location": user.location,
        "description": user.description
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
