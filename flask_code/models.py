from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/dbmp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # dont show case warnings on console
db=SQLAlchemy(app)

"""
student 

"""
