from flask import Blueprint, render_template

report_list = Blueprint('report_list', __name__, url_prefix='/')

@report_list.route('/list')
def send_page():
    return render_template('report_list.html')