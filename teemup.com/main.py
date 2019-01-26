from flask import Flask, render_template, request
#import sqlite3
#import click`

app = Flask(__name__)

@app.route("/")
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
