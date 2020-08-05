from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'
ENV='dev'

if ENV=='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:qt123123...@localhost/task_db'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b9d110edd60284:786168b2@us-cdbr-east-02.cleardb.com/heroku_1d93471d9d18b6f?reconnect=true'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@/mysql0820?unix_socket=/cloudsql/task-list-285414:us-central1:mysql0820'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
from routes import *

if __name__ == '__main__':
    app.run()
