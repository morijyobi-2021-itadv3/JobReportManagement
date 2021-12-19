from model.db import get_connection

conn = get_connection()

def insert_new_user():
  """
  新しいユーザーの追加
    Args:
      object: 追加するデータ
    Returns:
      bool: 成功したかどうか
  """

  cur = conn.cursor()
  cur.execute('INSERT INTO users (name,mail,is_newuser,user_type,created_at) values("test","test@morijyobi.ac.jp",TRUE,0,current_timestamp(0)')
  results = cur.fetchall()

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

  sql = 'SELECT max(id) FROM user;'

  cur = conn.cursor()
  cur.execute(sql)
  results = cur.fetchone() 

  cur.close()
  conn.close()
