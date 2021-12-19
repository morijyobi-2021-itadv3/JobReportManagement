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
  print(results)

  cur.close()
  conn.close()

  return results
