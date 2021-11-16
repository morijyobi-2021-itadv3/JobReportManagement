from flask import Flask, render_template
import db

app = Flask(__name__)

from report_list import report_list
app.register_blueprint(report_list)

@app.route("/")
def top():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)