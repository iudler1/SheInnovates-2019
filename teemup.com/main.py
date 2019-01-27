from flask import Flask, render_template, request
from db import session, User

app = Flask(__name__, static_folder="static")
"""
@app.route('/send', methods=['GET', 'POST'])
def send():
      if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            print(email + password)
            return render_template('success.html', email=email)

      return render_template('signin.html')
"""
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/signup.html", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
    return render_template("signup.html")

@app.route("/signin.html", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email + " " + password)
        #session.add()
        return render_template('home.html', email=email)
    return render_template("signin.html")

@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/account.html", methods=['GET', 'POST'])
def account():
    return render_template("account.html")

@app.route("/create.html", methods=['GET', 'POST'])
def create():
    return render_template("create.html")

@app.route("/find.html")
def find():
    return render_template("find.html")

@app.route("/yourEvents.html")
def yourEvents():
    return render_template("yourEvents.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
