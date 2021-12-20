from model.db import get_connection

conn = get_connection()

def insert_new_user(password,salt,name,mail,user_type):
  """
  新しいユーザーの追加
    Args:
      password(string): ハッシュ化されたパスワード
      salt(string): ランダムに生成されたソルト
      name(string): ユーザーの名前
      mail(string):ユーザーのメールアドレス
      user_type(int): ユーザータイプ
    Returns:
      bool: 成功したかどうか
  """

  sql = 'INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES (%s,%s,%s,%s,TRUE,%s)'

  cur = conn.cursor()
  results = cur.execute(sql,[mail,password,salt,name,user_type])

  cur.close()
  conn.close()

  return results

def get_latest_user_id():
  """
  現在の最新のユーザーIDを取得
    Args:
      なし
    Returns:
      int: 取得したID
  """

  sql = 'SELECT MAX(id) FROM user WHERE user_type = 0;'

  cur = conn.cursor()
  cur.execute(sql)
  id = cur.fetchone() 

  cur.close()
  conn.close()

  return id
