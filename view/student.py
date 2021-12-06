from flask import Blueprint, render_template

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/list')
def open_list():
    return render_template('student/report_list.html')

