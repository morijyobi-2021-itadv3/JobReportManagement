from crypt import methods
from select import select
from flask import Blueprint, render_template, request
from model.report import select_reports
from model.report import select_prefecture
from model.industries import select_industries
from model.students import select_graduation_year

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
        graduation = select_graduation_year();
        prefecture = select_prefecture();

        return render_template('student/report_list.html', report=reports, industry=industry, graduation=graduation, prefecture=prefecture)

    elif request.method == 'POST':
        print('aaa')


@student.route('/details')
def sample():
    id = request.args.get('id') # get送信時
    # id = request.form.get('id') # post送信時
    return render_template('student/sample.html', id=id)
