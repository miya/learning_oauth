import os
import tweepy
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.secret_key = "hogehoge"

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
CALLBACK_URL = os.environ.get("CALLBACK_URL")


# 認証用URLを生成する
def twitter_auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)
    try:
        redirect_url = auth.get_authorization_url()
        return redirect(redirect_url)
    except tweepy.TweepError:
        return render_template("error.html")


# ユーザー情報を取得する
def get_user_data(api):
    user = api.me()
    user_data_dic = {
        "id": user.id,
        "id_str": user.id_str,
        "name": user.name,
        "screen_name": user.screen_name,
        "location": user.location,
        "profile_location": user.profile_location,
        "description": user.description,
        "url": user.url,
        "protected": user.protected,
        "followers_count": user.followers_count,
        "friends_count": user.friends_count,
        "listed_count": user.listed_count,
        "created_at": user.created_at,
        "favourites_count": user.favourites_count,
        "utc_offset": user.utc_offset,
        "time_zone": user.time_zone,
        "geo_enabled": user.geo_enabled,
        "verified": user.verified,
        "statuses_count": user.statuses_count,
        "lang": user.lang,
        "contributors_enabled": user.contributors_enabled,
        "is_translator": user.is_translator,
        "is_translation_enabled": user.is_translation_enabled,
        "profile_background_color": user.profile_background_color,
        "profile_background_image_url": user.profile_background_image_url,
        "profile_background_image_url_https": user.profile_background_image_url_https,
        "profile_background_tile": user.profile_background_tile,
        "profile_image_url": user.profile_image_url,
        "profile_image_url_https": user.profile_image_url_https,
        "profile_banner_url": user.profile_banner_url,
        "profile_link_color": user.profile_link_color,
        "profile_sidebar_border_color": user.profile_sidebar_border_color,
        "profile_sidebar_fill_color": user.profile_sidebar_fill_color,
        "profile_text_color": user.profile_text_color,
        "profile_use_background_image": user.profile_use_background_image,
        "has_extended_profile": user.has_extended_profile,
        "default_profile": user.default_profile,
        "default_profile_image": user.default_profile_image,
        "following": user.following,
        "follow_request_sent": user.follow_request_sent,
        "notifications": user.notifications,
        "translator_type": user.translator_type,
        "suspended": user.suspended,
        "needs_phone_verification": user.needs_phone_verification,
    }
    return user_data_dic


@app.route("/")
def root():
    return render_template("hello.html")


@app.route("/", methods=["POST"])
def login():
    return twitter_auth()


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
