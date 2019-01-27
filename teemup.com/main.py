from flask import Flask, render_template, request
from db import session, User

app = Flask(__name__, static_folder="static")

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")
    
@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/account.html")
def account():
    return render_template("account.html")

@app.route("/create.html")
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
