from flask_code.models import  db

"""
college-- Address 1--1
Department -- students --1-M
student -- subject -- MM
"""

class College(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column("id",db.Integer,primary_key=True)
    clgname = db.Column('clg_name',db.String(100))
    clgcode = db.Column('clg_code',db.String(100))
    active =db.Column("active",db.String(10),default ='y')
    adrref = db.relationship("Address",backref="clgref",lazy=False,uselist=False)

class Address(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("city",db.String(100))
    state = db.Column("state",db.String(100))
    pincode =db.Column('pin_code',db.Integer)
    college = db.Column("clg_id",db.ForeignKey("college.id"),unique=True,nullable=False)
    active = db.Column("active", db.String(10), default='y')


