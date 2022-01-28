from datetime import timedelta
from flask import Flask, render_template, redirect, request, session, abort
import os
from model import db
from model.hash import generate_random_alpha, sha256_text
from model.mail import smtp_send_mail
from model.user import user_login, is_exist_mail, get_token

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]
app.permanent_session_lifetime = timedelta(hours=1)


@app.route("/")
def index():
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
    # try:
    print('load')
    mail = request.form.get("email")
    password = request.form.get("password")
    login_result = user_login(mail, password)
    print(login_result)
    if login_result:
        session.permanent = True
        user = {}
        print(login_result[0])
        user['id'] = login_result[0]
        user['name'] = login_result[4]
        user['permission'] = login_result[6]

        # セッションの保持
        session['user'] = user
        # TODO:各マイページへ遷移する
        print(user['permission'])
        if user['permission'] == 0:
            return redirect('/student/home')
        elif user in [1, 2]:
            return redirect('/teacher')

    elif login_result is None:
        return render_template('index.html', errormsg="パスワードまたはメールアドレスが間違っています", mail=mail)
    else:
        return render_template('index.html', errortxt="エラーが発生しました。", mail=mail)
    # except Exception as e:
    #     print(e.args)
    #     # TODO: サーバーエラー時のページ表示をする
    #     abort(500)


@app.route("/reset_password")
def reset_password():
    return render_template('reset_password.html')


@app.route("/sent_mail")
def sent_mail():
    return render_template('send_mail.html')


@app.route("/reset_password", methods=["POST"])
def reset_password_post():
    mail = request.form.get("email")
    token = get_token(mail)
    if token:
        smtp_send_mail(mail,
                       """
            <h1>報告書管理システム</h1>
            <p>次のリンクを使ってパスワードをリセットしてください</p><br>
            <p><a href="http://localhost:5001/password_edit/{0}">http://localhost:5001/password_edit/{0}</a></p>
                   
            """.format(token)
                       )
    else:
        smtp_send_mail(mail,
                       """
            <h1>報告書管理システム</h1>
            <p>このメールアドレスは登録されていません。</p>
        """
                       )

    return render_template('sent_mail.html', mail=mail)


def logout():
    """
    ログアウト処理を行うメソッド。
    return:メインページへ
    """
    session.pop("user", None)
    return redirect('/')
