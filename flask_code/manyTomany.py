"""from gitsample.flask_code.models import  db,Student





class stud_subj(db.Model):
    __table_args__ = {'extend_existing': True}
    stud_id=db.Column('stud_id', db.ForeignKey("student.stud_id"), primary_key=True)
    subj_id=db.Column('subj_id', db.ForeignKey("subject.subj_id"), primary_key=True)

class Subject(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column('subj_id', db.Integer(), primary_key=True)
    name = db.Column('subj_nm', db.String(100))
    Active = db.Column('active', db.String(50),default='y')
    studsref = db.relationship("Student", secondary=stud_subj,backref='subjs', lazy=True)
"""