from model.db import get_connection

conn = get_connection()

def insert_new_user(name,mail,user_type):
  """
  新しいユーザーの追加
    Args:
      name(string): ユーザーの名前
      mail(string):ユーザーのメールアドレス
      user_type(int): ユーザータイプ
    Returns:
      bool: 成功したかどうか
  """

  sql = 'INSERT INTO users (name,mail,is_newuser,user_type,created_at) VALUES (%s,%s,TRUE,%s,current_timestamp(0))'

  cur = conn.cursor()
  results = cur.execute(sql,[name,mail,user_type])

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

  sql = 'SELECT MAX(id) FROM user;'

  cur = conn.cursor()
  cur.execute(sql)
  results = cur.fetchone() 

  cur.close()
  conn.close()
