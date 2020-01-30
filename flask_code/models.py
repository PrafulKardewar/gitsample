from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@123@localhost/dbmp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # dont show case warnings on console
db=SQLAlchemy(app)

"""
coll- addre= 1-1
Depa -student 1-m
"""

class Department(db.Model):
    dep_id=db.Column(db.Integer(),primary_key=True)
    dep_name=db.Column(db.String(100))
    dep_sub=db.Column(db.String(100))
    active=db.Column(db.String(10))
    studsref=db.relationship('Student',backref='depref',lazy=True,uselist=True)

class Student(db.Model):
    stud_id=db.Column(db.Integer(),primary_key=True)
    stud_name=db.Column(db.String(100))
    stud_marks=db.Column(db.Integer())
    active = db.Column(db.String(10))
    depId=db.Column(db.ForeignKey('department.dep_id'),unique=False,nullable=True)


if __name__ == '__main__':
    db.create_all()