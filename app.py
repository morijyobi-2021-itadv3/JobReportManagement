from flask import Flask,Blueprint, render_template
from add_user import add_user_bp
import db

app = Flask(__name__)

app.register_blueprint(add_user_bp)

@app.route("/")
def top():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)