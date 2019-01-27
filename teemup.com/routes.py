import app
from flask import Flask, render_template, request


@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/account/")
def account():
    return render_template("account.html")

@app.route("/create/")
def create():
    return render_template("create.html")

@app.route("/find/")
def find():
    return render_template("find.html")

@app.route("/yourEvents/")
def yourEvents():
    return render_template("yourEvents.html")


