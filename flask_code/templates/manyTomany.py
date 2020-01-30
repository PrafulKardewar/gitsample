from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


third_table_ref = db.Table("stud_subj",
        db.Column('stud_id',db.ForeignKey("student.stud_id"),primary_key=True),
        db.Column('subj_id',db.ForeignKey("subject.subj_id"), primary_key=True))


class Student(db.Model):
    id = db.Column('stud_id',db.Integer(),primary_key=True)
    name = db.Column('stud_nm',db.String(100))
    marks=db.Column('stud_marks',db.String(100))
    Active=db.Column('active',db.String(50),default='y')

class Subject(db.Model):

    id = db.Column('subj_id', db.Integer(), primary_key=True)
    name = db.Column('subj_nm', db.String(100))
    Active = db.Column('active', db.String(50),default='y')
    studsref = db.relationship("Student", secondary=third_table_ref,backref='subjs', lazy=True)

if __name__ == '__main__':
        db.create_all()