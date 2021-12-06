from flask import Flask, Blueprint, render_template, request
import csv


teacher_bp = Blueprint('teacher',__name__, url_prefix='/teacher')

@teacher_bp.route('/add_user',methods=['GET','POST'])
def send_first_page():
  if(request.method == 'GET'):
    return render_template('add_user.html')
  else:
    csvdata = request.files['csv']
    result = csv.reader(csvdata)
    for data in result:
      print(data)
    return render_template('index.html')
