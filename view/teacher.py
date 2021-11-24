from flask import Flask, Blueprint, render_template


teacher_bp = Blueprint('teacher',__name__, url_prefix='/teacher')

@teacher_bp.route('/add_user',methods=['GET'])
def add_user():
  return render_template('add_user.html')