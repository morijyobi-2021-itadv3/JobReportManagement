from datetime import timedelta
from flask import Flask, render_template, redirect, request, session, abort
import os
from model.user import user_login

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]
app.permanent_session_lifetime = timedelta(hours=1)


@app.route("/")
def top():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/login")
def no_post_login():
    """
    POSTがない場合のログイン
    :return:
    """
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    """
    ログイン処理をするメソッド
    return:
        ログイン成功時、ログインしたuser_typeに対応したマイページへ遷移
        ログイン失敗時、メインページ"/"へリダイレクトする。
    """
    try:
        mail = request.get("email")
        password = request.get("password")
        login_result = user_login(mail, password)
        if login_result:
            session.permanent = True
            user = []
            user['id'] = login_result[0][0]
            user['name'] = login_result[0][4]
            user['permission'] = login_result[0][6]

            # セッションの保持
            session['user'] = user
            # TODO:各マイページへ遷移する

        else:
            return redirect('/')

    except Exception:
        # TODO: サーバーエラー時のページ表示をする
        abort(500)


@app.route("/reset_password")
def reset_password():
    return render_template('reset_password.html')


@app.route("/send_mail")
def send_mail():
    return render_template('send_mail.html')


@app.route("/sent_mail", methods=["POST"])
def sent_mail():
    mail = request.get("email")
    return render_template('sent_mail.html', mail)


@app.route("/change_password", methods=["POST"])
def change_password():
    # TODO: マイページに遷移する
    return redirect()


def logout():
    """
    ログアウト処理を行うメソッド。
    return:メインページへ
    """
    session.pop("user", None)
    return redirect('/')
