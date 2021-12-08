from flask import Flask, Blueprint, render_template, request
import csv
import io

teacher_bp = Blueprint('teacher',__name__, url_prefix='/teacher')

@teacher_bp.route('/add_user',methods=['GET','POST'])
def send_first_page():
  if(request.method == 'GET'):
    return render_template('add_user.html')
  else:
    csvdata = request.files.get('csv')
    result = []
    for row in csvdata:
      rowdata = [data.strip() for data in row.decode(encoding='shift-jis').split(',')]
      print(rowdata)
      

    # print(csvdata)
    # print(type(csvdata.stream))
    # text_stream = io.TextIOWrapper(csvdata.stream, encoding="utf-8")
    # for data in csv.reader(text_stream):
    #   print(data)

    return render_template('index.html')
