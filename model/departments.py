from model.db import get_connection
import psycopg2

def get_departments_visible():
  """
  「表示」設定の学科情報を取得
  Args:
    なし
  Returns:
    Array: 学科情報を含んだ配列
  """

  conn = get_connection()
  
  sql = 'SELECT * FROM departments WHERE is_show = TRUE;'
  
  cur = conn.cursor()
  cur.execute(sql)
  departments = cur.fetchall() 

  cur.close()
  conn.close()

  return departments

def get_departmentId_with_name(department_name):
  """
  学科名をもとに学科IDを取得
  Args:
    department_name(string): 学科名
  Returns:
    Int: 学科ID
  """

  conn = get_connection()

  sql = "SELECT id FROM departments WHERE name = %s;"

  cur = conn.cursor()
  cur.execute(sql,[department_name])
  department_id = cur.fetchone()

  cur.close()
  conn.close()

  return department_id
