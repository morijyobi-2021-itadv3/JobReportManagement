from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route("/")
def top():
    samples = db.select_sample()
    return render_template('index.html', samples=samples)

if __name__ == "__main__":
    app.run(debug=True)