from flask import Flask, Blueprint, render_template
from view.teacher import teacher_bp
from model.db import select_sample

app = Flask(__name__)

app.register_blueprint(teacher_bp)

@app.route("/")
def top():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)