from flask import Blueprint
from datetime import timedelta

from flask import Flask, render_template, redirect, request, session, abort
import os
from model import db
from model.hash import generate_random_alpha, sha256_text
from model.send_mail import smtp_send_mail
from model.user import user_login, is_exist_mail, get_token, find_reset_token, rechange_password, set_password
from flask import Flask, Blueprint, render_template
from view.teacher import teacher_bp
from model.db import get_connection

common = Blueprint('common', __name__, url_prefix='/common')


@common.route('/login')
def no_post_login():
    """
    POSTがない場合のログイン
    :return:
    """
    return redirect('/')


@common.route('/login', methods=['POST'])
def login():
    """
    ログイン処理をするメソッド
    return:
        ログイン成功時、ログインしたuser_typeに対応したマイページへ遷移
        ログイン失敗時、メインページ'/'へリダイレクトする。
    """
    # try:
    print('load')
    mail = request.form.get('email')
    password = request.form.get('password')
    login_result = user_login(mail, password)
    print(login_result)

    if login_result[5]:
        session.permanent = True
        user = {'id': login_result[0]}
        session['new_user'] = user
        return render_template('new_password.html', pgmsg='初めてログインした場合、パスワード変更が必要です。')

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
            return redirect('/student')
        elif user in [1, 2]:
            return redirect('/teacher')

    elif login_result is None:
        return render_template('index.html', errormsg='パスワードまたはメールアドレスが間違っています', mail=mail)
    else:
        return render_template('index.html', errormsg='エラーが発生しました。', mail=mail)
    # except Exception as e:
    #     print(e.args)
    #     # TODO: サーバーエラー時のページ表示をする
    #     abort(500)


@common.route('/reset_password')
def reset_password():
    return render_template('reset_password.html')


@common.route('/sent_mail')
def sent_mail():
    return render_template('send_mail.html')


@common.route('/reset_password', methods=['POST'])
def reset_password_post():
    mail = request.form.get('email')
    token = get_token(mail)
    if token:
        smtp_send_mail(mail, '[No reply]パスワードリセットの通知',
                       '''
            <h1>報告書管理システム</h1>
            <p>次のリンクを使ってパスワードをリセットしてください</p><br>
            <p><a href='http://{0}/{1}?id={2}'>http://{0}/{1}?id={2}</a></p>

            '''.format(os.environ['WEB_URL'], token[0], token[1])
                       )
    else:
        smtp_send_mail(mail, '[No reply]パスワードリセットの通知',
                       '''
            <h1>報告書管理システム</h1>
            <p>このメールアドレスは登録されていません。</p>
        '''
                       )

    return render_template('sent_mail.html', mail=mail)


@common.route('/change_password/<token>', methods=['GET'])
def change_password_get(token):
    user_id = request.args.get('id', '')
    find_id = find_reset_token(token, user_id)
    if find_id:
        session['reset_userid'] = user_id
        session['reset_id'] = find_id
        return render_template('new_password.html')
    else:
        return render_template('index.html', errormsg='不正なリクエストです', mail='')


@common.route('/change_password', methods=['POST'])
def change_password():
    password = request.form.get('password')
    if session['new_user']:
        errmsg = set_password(password, session['new_user']['id'])
        if errmsg:
            return render_template('index.html', pgmsg=errmsg)
        else:
            return render_template('index.html', pgmsg='パスワードを変更しました')

    errmsg = rechange_password(password, session['reset_id'], session['reset_userid'])

    if errmsg:
        return render_template('index.html', pgmsg=errmsg)
    else:
        print('error')
        return render_template('index.html', pgmsg='パスワードを変更しました')


def logout():
    """
    ログアウト処理を行うメソッド。
    return:メインページへ
    """
    session.pop("user", None)
    return redirect('/')

