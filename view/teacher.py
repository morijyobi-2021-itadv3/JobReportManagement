from flask import Flask, Blueprint, render_template, request
import csv
import io
from model.departments import get_departments_visible
from model.user import insert_new_user
from model.user import get_latest_user_id
teacher_bp = Blueprint('teacher',__name__, url_prefix='/teacher')

@teacher_bp.route('/add_user',methods=['GET','POST'])
def add_user():
  if(request.method == 'GET'):
    # 学科コース名を取得する
    departments = get_departments_visible()
    return render_template('add_user.html',departments=departments)
  else:
    # 送信された各種データの取得
    csvdata = request.files.get('csv')
    user_type = request.form.get('user-type')
    department = request.form.get('department')
    user_type_number = None

    if(user_type == '学生'):
      user_type_number = 0
    elif(user_type == '教員'):
      user_type_number = 1
    elif(user_type == '就職課'):
      user_type_number = 2
    
    # 取得したCSVデータを二次元配列に格納
    csvDataMatrix = [[data.strip() for data in row.decode(encoding='shift-jis').split(',')] for row in csvdata]
    
    # のちに使いやすいように[{},{}]辞書型にする
    # 辞書型のkeyとなる部分の配列
    header = [data for data in csvDataMatrix[0]]
    # csvデータの整形(必要のない１行目の削除)
    del csvDataMatrix[0]

    # 辞書型データが格納された配列
    dictionaryArray = []
    for row in csvDataMatrix:
      dataObj = {}
      for index in range(len(row)):
        dataObj.setdefault(header[index],row[index])
      dictionaryArray.append(dataObj)

    add_new_users(dictionaryArray,user_type_number,department)

    return render_template('index.html')

def add_new_users(dictionaryArray,user_type_number,department):
  """
  新しいUsersデータを追加
  Args: 
    matrix(array): 追加したいcsvデータの二次元配列
    user_type_number: 追加するユーザータイプの数字
    department: 学科名
  Returns:
    bool: 成功したかどうか
  """

  # 1行ずつデータを追加
  for userData in dictionaryArray:
    insert_new_user(userData['氏名'],userData['メールアドレス'],user_type_number)
    # ユーザータイプが「学生」の時の処理
    if(user_type_number == 0):
      # 最新のユーザーIDを取得
      id = get_latest_user_id()
      
      #studentテーブルにデータを追加する処理


