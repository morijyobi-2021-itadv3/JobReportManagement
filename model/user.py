import datetime

from model.db import get_connection
from model.hash import generate_random_alpha, sha256_text

# constant args

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
    if id[0]:
        cur.close()
        cur = conn.cursor()
        token = generate_random_alpha(64)
        now_date = datetime.datetime.now()
        day_later = now_date + datetime.timedelta(days=1)

        cur.execute('INSERT INTO change_passwords(user_id, hash, exp_datetime, updated_at) VALUES(%s,%s,%s,%s) ',
                    (id, sha256_text(str(token), str(id[0])), now_date, day_later))
        conn.commit()
        cur.close()
        conn.close()
        return token

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

    conn = db.connect_sql()
    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE mail = (%s)', (mail,))
    id = cur.fetchone()
    return id or None
