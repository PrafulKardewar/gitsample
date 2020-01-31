from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@123@localhost/dbmp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # dont show case warnings on console
db=SQLAlchemy(app)

#app.config['SECRET_KEY'] = '8r884uru44u8999u9ioiere8r'
#from gitsample.flask_code.oneToOneModel import *
#from gitsample.flask_code.manyTomany import *
"""
coll- addre= 1-1
Depa -student 1-m
"""



class Department(db.Model):
    __table_args__ = {'extend_existing': True}
    dep_id=db.Column(db.Integer(),primary_key=True)
    dep_name=db.Column(db.String(100))
    dep_strength=db.Column(db.Integer())
    active=db.Column(db.String(10),default='Y')
    studsref=db.relationship('Student',backref='depref',lazy=True,uselist=True)

#d1=Department(dep_id=1,dep_name='ENTC',dep_strength=100)
class Student(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column('stud_id',db.Integer(),primary_key=True)
    name = db.Column('stud_nm',db.String(100))
    marks=db.Column('stud_marks',db.String(100))
    Active=db.Column('active',db.String(50),default='y')
    depId=db.Column(db.ForeignKey('department.dep_id'),unique=False,nullable=True,)

if __name__ == '__main__':
   pass
   # db.create_all()