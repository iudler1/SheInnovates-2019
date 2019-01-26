from flask import Flask, render_template, request
#import sqlite3
#import click`

app = Flask(__name__)

import routes

if __name__ == '__main__':
  app.run(host='0.0.0.0')
