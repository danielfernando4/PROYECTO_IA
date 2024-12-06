"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hellow world!!!!"

@app.route('/hello')
def hello():
    return "siuuuu"


@app.route('/siu/<name>')
def siu(name):
    return f"hellow {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
"""

"""
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("loginRegister.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('loginRegister.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)


