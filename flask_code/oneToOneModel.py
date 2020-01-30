from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/dbmp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # dont show case warnings on console
db=SQLAlchemy(app)

"""
college-- Address 1--1
Department -- students --1-M
student -- subject -- MM
"""

class College(db.Model):
    id = db.Column("id",db.Integer,primary_key=True)
    clgname = db.Column('clg_name',db.String(100))
    clgcode = db.Column('clg_code',db.String(100))
    active =db.Column("active",db.String(10),default ='y')
    adrref = db.relationship("Address",backref="clgref",lazy=False,uselist=False)

class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city",db.String(100))
    state = db.Column("state",db.String(100))
    pincode =db.Column('pin_code',db.Integer)
    college = db.Column("clg_id",db.ForeignKey("college.id"),unique=True,nullable=False)
    active = db.Column("active", db.String(10), default='y')


if __name__ == '__main__':
    db.create_all()
    print("Table created")