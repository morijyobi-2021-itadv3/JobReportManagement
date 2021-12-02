from flask import Flask, render_template
from model.db import select_sample

app = Flask(__name__)

@app.route("/")
def top():
    datas = select_sample()
    return render_template('index.html', data=datas)

if __name__ == "__main__":
    app.run(debug=True)
