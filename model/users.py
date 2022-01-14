from model.db import get_connection

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

  conn = get_connection()

  sql = 'INSERT INTO users (mail, password, salt, name, is_newuser, user_type) VALUES (%s,%s,%s,%s,TRUE,%s)'

  cur = conn.cursor()
  results = cur.execute(sql,[mail,password,salt,name,user_type])
  conn.commit()

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

  conn = get_connection()

  sql = 'SELECT MAX(id) FROM users WHERE user_type = 0;'

  cur = conn.cursor()
  cur.execute(sql)
  id = cur.fetchone() 

  cur.close()
  conn.close()

  return id

def get_userId_with_mail(mail):
  """
  メールアドレスからユーザIDを取得
    Args:
      mail(string): メールアドレス
    Returns:
      id(int): ユーザーID
  """

  conn = get_connection()

  sql = 'SELECT id FROM users WHERE mail = %s;'

  cur = conn.cursor()
  cur.execute(sql,[mail])
  id = cur.fetchone() 

  cur.close()
  conn.close()

  return id

def get_teacher_info():
  """
  教員情報を取得
    Args: 
      なし
    Returns: 
      Array: 教員情報の配列(メール,名前)
  """

  conn = get_connection()

  sql = 'SELECT mail,name from users WHERE user_type = 1 ORDER BY id'

  cur = conn.cursor()
  cur.execute(sql)
  result = cur.fetchall()

  cur.close()
  conn.close()

  return result
