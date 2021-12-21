from model.db import get_connection

def insert_new_student(user_id,graduation_year,student_number,department_id,teacher_id):
  """
  新しいユーザーの追加
    Args:
      user_id(int): 紐づくユーザーID
      graduation_year(int): 卒業年度
      student_number(int): 学生番号
      department_id(int): 紐づく学科ID
      teacher_id(int): 紐づく教員(担任)ID
    Returns:
      bool: 成功したかどうか
  """

  conn = get_connection()
  
  sql = 'INSERT INTO students VALUES (%s,%s,%s,%s,%s);'

  cur = conn.cursor()
  results = cur.execute(sql,[user_id,graduation_year,student_number,department_id,teacher_id])
  conn.commit()

  cur.close()
  conn.close()

  return results
