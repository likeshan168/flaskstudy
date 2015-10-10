#import the necessary modules
import sqlite3
from flask import Flask, request, session,g,redirect,url_for, abort, render_template,flask

#config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'shermanli'
USERNAME = 'admin'
PASSWORD = 'default'

#create the app
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run()
