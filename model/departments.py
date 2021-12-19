from model.db import get_connection

conn = get_connection()

def get_departments_visible():
  """
  「表示」設定の学科情報を取得
  Args:
    なし
  Returns:
    Array: 学科情報を含んだ配列
  """
  sql = 'SELECT * FROM departments WHERE is_show = TRUE;'
  cur = conn.cursor()
  cur.execute(sql)
  departments = cur.fetchall() 

  cur.close()
  conn.close()

  return departments
