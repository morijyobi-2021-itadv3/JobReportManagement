from types import resolve_bases
from flask import Flask, Blueprint, render_template, request, redirect, jsonify
from model.departments import get_departments_visible,get_departmentId_with_name
from model.users import get_teacher_info, insert_new_user,get_latest_user_id,get_userId_with_mail
from model.students import insert_new_student
from model.hash import sha256_text,generate_random_alpha
from model.mail import send_mail

teacher_bp = Blueprint('teacher',__name__, url_prefix='/teacher')

@teacher_bp.route('/add_user',methods=['GET','POST'])
def add_user():
  error_text = ''
  if(request.method == 'GET'):
    # 学科コース名を取得する
    try: 
      departments = get_departments_visible()
    except Exception as e:
      error_text = '学科コースを取得できませんでした' 
      print(e)
      
    return render_template('add_user.html',departments=departments,error_text=error_text)
    
  else:
    # 送信された各種データの取得
    csvdata = request.files.get('csv')
    user_type = request.form.get('user-type')
    department = request.form.get('department')

    try:
      department_id = get_departmentId_with_name(department)
    except Exception as e:
      print(e)

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

    # ユーザーの新規追加
    try:
      error_list = add_new_users(dictionaryArray,user_type_number,department_id)
    except Exception as e:
      print(e)
      

    return render_template('index.html',error_list=error_list)

def add_new_users(dictionaryArray,user_type_number,department_id):
  """
  新しいUsersデータを追加
  Args: 
    matrix(array): 追加したいcsvデータの二次元配列
    user_type_number: 追加するユーザータイプの数字
    department_id: 学科ID
  Returns:
    Array: 失敗したデータが含まれた配列(ないときは空の配列)
  """

  # errorのデータを格納する配列 
  error_list = []

  # 1行ずつデータを追加
  for userData in dictionaryArray:
    password = generate_random_alpha(10)
    salt = generate_random_alpha(5)
    hashedPassword = sha256_text(password,salt)
    
    try:
      insert_new_user(hashedPassword,salt,userData['氏名'],userData['メールアドレス'],user_type_number)
    except Exception as e:
      print(e)

    #　登録されたメールアドレス宛に、ランダムに生成したパスワード(仮)を送信する
    # 誤送信を防ぐためにコメントアウトしておく
    # send_mail(userData['メールアドレス'],password)
    
    # 学生のデータを追加
    if(user_type_number == 0):
      try: 
        # 最新のユーザーIDを取得
        id = get_latest_user_id()

        # 担任IDを取得
        teacher_id = get_userId_with_mail(userData['担任名メールアドレス'])
        
        #　studentテーブルにデータを追加する処理
        insert_new_student(id,userData['卒業年度'],userData['学籍番号'],department_id,teacher_id)
      except Exception as e :
        error_info = {'name': userData['氏名'], 'mail': userData['メールアドレス']}
        error_list.append(error_info)
        print(e)

  return error_list

@teacher_bp.route('/add_user/api/teacher_info',methods=['GET'])
def get_teacher_info_api():

  try:
    # 教員の名前とメールのデータを取得する
    teacher_info_array = get_teacher_info()
  except Exception as e:
    print(e)

  # オブジェクトにする
  teacher_info_obj = {}
  for data in teacher_info_array:
    teacher_info_obj[data[0]] = data[1]
  
  # オブジェクトをJSONに変換する
  result_json = jsonify(teacher_info_obj)

  return result_json
