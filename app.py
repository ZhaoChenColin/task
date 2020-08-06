from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'
ENV='prod'

if ENV=='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:qt123123...@localhost/task_db'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ba7a4a4debe9a0:dcd84155@us-cdbr-east-02.cleardb.com/heroku_2e33ed2154863c6'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
from routes import *

if __name__ == '__main__':
    app.run()
