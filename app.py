from flask import Flask, render_template
from model.db import select_sample

app = Flask(__name__)

@app.route("/")
def top():
    
    return render_template('index.html',data = select_sample())

if __name__ == "__main__":
    app.run(debug=True)