from flask import Blueprint, render_template
from model.report import select_all

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/list')
def open_list():
    datas = select_all()
    return render_template('student/report_list.html', datas=datas)

