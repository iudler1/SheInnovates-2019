from flask import Flask, render_template, request
from db import session, User

app = Flask(__name__, static_folder="static")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/find")
def find():
    return render_template("find.html")

@app.route("/yourEvents")
def yourEvents():
    return render_template("yourEvents.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
