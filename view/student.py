from crypt import methods
from flask import Blueprint, render_template, request
from model.report import select_reports
from model.industries import select_industries

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/list', methods=['GET','POST'])
def open_list():
    if request.method == 'GET':
        datas = select_reports()

        num = 0
        reports = []

        while num < len(datas) -1:
            if datas[num][0] != datas[num+1][0]:
                reports.append(datas[num])
            num += 1            
            
        reports.append(datas[num])

        industry = select_industries();

        return render_template('student/report_list.html', report=reports, industry=industry)

    elif request.method == 'POST':
        print('aaa')


@student.route('/details')
def sample():
    id = request.args.get('id') # get送信時
    # id = request.form.get('id') # post送信時
    return render_template('student/sample.html', id=id)
