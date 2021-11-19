from flask import Flask, Blueprint, render_template


add_user_bp = Blueprint('add_user',__name__, url_prefix='/add_user')

@add_user_bp.route('/',methods=['GET'])
def add_user():
  return render_template('add_user.html')