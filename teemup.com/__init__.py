from flask import Flask, render_template, request
from flask_redis import Redis
import SQLAlchemy

#import sqlite3
#import click`

app = Flask(__name__)

db = Redis('localhost')

if __name__ == '__main__':
  app.run(host='0.0.0.0')

import routes
