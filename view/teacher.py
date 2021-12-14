from flask import Flask, Blueprint, render_template, request
import csv
import io
from model.db import select_sample
teacher_bp = Blueprint('teacher',__name__, url_prefix='/teacher')

@teacher_bp.route('/add_user',methods=['GET','POST'])
def send_first_page():
  if(request.method == 'GET'):
    # 学科コース名を取得する
    departments = select_sample()
    return render_template('add_user.html',departments=departments)
  else:
    #送信された各種データの取得
    csvdata = request.files.get('csv')
    user_type = request.form.get('user-type')
    department = request.form.get('department')

    print(user_type)
    print(department)
    
    # 取得したCSVデータを二次元配列に格納
    csvDataMatrix = [[data.strip() for data in row.decode(encoding='shift-jis').split(',')] for row in csvdata]

    return render_template('index.html')
