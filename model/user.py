import datetime

from model.db import get_connection
from model.hash import generate_random_alpha, sha256_text

# constant args
from model.time_conversion import utc_now

ALPHA_LENGTH = 64
DAY_OF_SEC = 86400000


def user_login(mail, password):
    """ログインするためのメソッド
       Args:
           mail:Tokenを発行したいメールアドレス
           password:パスワードの平文
       Returns:
           Any:DBから取得してきたユーザーデータ
           mailが空の時は　None
    """

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT salt FROM users WHERE mail = (%s)', (mail,))
    sql_result = cur.fetchone()
    if not sql_result:
        return None
    salt = sql_result[0]
    cur.execute('SELECT * FROM users WHERE mail = (%s) AND password = (%s)', (mail, sha256_text(password, salt),))
    user = cur.fetchone()

    if user:
        return user

    return None


def get_token(mail):
    """パスワードを再発行したいアカウントの変更用Tokenを発行する

       Args:
           mail:Tokenを発行したいメールアドレス

       Returns:
           string: 64文字の大文字小文字含む英数字
           mailが空の時は　None
    """

    conn = get_connection()

    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE mail = (%s)', (mail,))
    id = cur.fetchone()

    if id:
        cur.close()
        cur = conn.cursor()
        token = generate_random_alpha(64)
        now_date = utc_now()
        day_later = now_date + datetime.timedelta(days=1)

        cur.execute('INSERT INTO change_passwords(user_id, hash, exp_datetime, updated_at) VALUES(%s,%s,%s,%s) ',
                    (id, sha256_text(str(token), str(id[0])), day_later, now_date))
        conn.commit()
        cur.close()
        conn.close()
        return [token, id[0]]

    cur.close()
    conn.close()
    return None


def is_exist_mail(mail):
    """
    メールが存在するかを判別する
    Args:
        mail: メールアドレス
    Returns:
        bool: 存在可否
    """

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE mail = (%s)', (mail,))
    id = cur.fetchone()
    cur.close()
    conn.close()
    return id or None


def find_reset_token(token, id):
    """

    Args:
        token:　リセット時に生成したトークン
        id:　ユーザーID

    Returns:
        id 若しくは None
        id: 配列の0番目にchange_passwordsのID
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        'SELECT id FROM change_passwords WHERE user_id = (%s) and hash = (%s) and is_changed = false and exp_datetime > (%s)',
        (id, sha256_text(token, id), utc_now()))
    id = cur.fetchone()
    cur.close()
    conn.close()
    return id or None


def rechange_password(password, reset_id, user_id):
    """

    Args:
        password: パスワード平文
        reset_id: change_passwordsテーブルのid
        user_id: usersのid

    Returns:
        None 若しくは　String
        エラーの場合はStringが返される

    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('UPDATE change_passwords SET is_changed = true  WHERE id = (%s)', (reset_id,))
        conn.commit()
        cur.close()
        cur = conn.cursor()
        salt = generate_random_alpha(64)
        res = cur.execute('UPDATE users SET password = (%s), salt = (%s) WHERE id = (%s)',
                          (sha256_text(password, salt), salt, user_id), )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        return "エラーが発生しました。"

    return None


def set_password(password, user_id):
    """

    Args:
        password: パスワード平文
        user_id: usersのid

    Returns:
        None 若しくは　String
        エラーの場合はStringが返される

    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        salt = generate_random_alpha(64)
        cur.execute('UPDATE users SET password = (%s), salt = (%s),is_newuser = false WHERE id = (%s)',
                          (sha256_text(password, salt), salt, user_id), )
        conn.commit()
        cur.close()


        conn.close()
    except Exception as e:
        print(e)
        return "エラーが発生しました。"


    return None