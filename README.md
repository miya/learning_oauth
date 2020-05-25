# learning_twitter_oauth

TwitterのOAuth認証について学んだのでFlaskとTweepyで実装してみたやつ。
アクセストークンをゲットして[UserObject](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object)を表示させるWebアプリ。

## What is OAuth

<img src=https://user-images.githubusercontent.com/34241526/82755818-0f818300-9e11-11ea-98a2-7ca90361d0c1.png width=70% alt="">

1. クライアントアプリを使いたい
2. アクセストークンを要求
3. 要求している権限を与えるかどうかの認証画面をリダイレクト
4. 許可する
5. アクセストークンを発行
6. アクセストークンを含めてリクエスト
7. ユーザーのデータを利用する権限をアクセスートンが持っていたら要求されたデータを返す

## How to use
1. [TwitterDeveloper](https://developer.twitter.com/en)でAPIの利用申請をする
2. 承認後、API keyとAPI secret keyをメモして`app.py`のCONSUMER_KEYとCONSUMER_SECRETに代入するか、環境変数に入れておく
3. ローカルで動かすので`http://0.0.0.0:8080/callback` をTwitterDeveloperのCallback URLに入れる
4. `git clone https://github.com/miya/learning_twitter_oauth`でこのリポジトリをクローン
5. `cd src`でapp.pyがあるディレクトリに移動
6. `python3 app.py`でアプリの起動

## Demo

<img src=https://raw.githubusercontent.com/wiki/miya/learning_twitter_oauth/images/output.gif width=70% alt="">

## References
* [一番わかりやすい OAuth の説明](https://qiita.com/TakahikoKawasaki/items/e37caf50776e00e733be)
* [認証に関するチュートリアル](https://kurozumi.github.io/tweepy/auth_tutorial.html)
