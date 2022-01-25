from flask import Blueprint, render_template, request
from model.report import select_all

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/list')
def open_list():
    datas = select_all()

    num = 0
    reports = []

    while num < len(datas) -1:
        if datas[num][0] != datas[num+1][0]:
            reports.append(datas[num])
        num += 1            
        
    reports.append(datas[num])

    return render_template('student/report_list.html', report=reports)

@student.route('/details')
def sample():
    id = request.args.get('id') # get送信時
    # id = request.form.get('id') # post送信時
    return render_template('student/sample.html', id=id)
