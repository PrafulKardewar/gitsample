from flask_code.dao_stud_dep import DepService,StudService
from flask_code.models import  db,Department,Student



class DepDaoimple(DepService):


    def get_single_dep(self,dep_id):
        dep=Department.query.filter_by(dep_id=dep_id).first()
        if dep:
            return dep


    def add_dep(self,dep):
        #dept=DepService.get_single_dep(dep.dep_id)
        print(dep.dep_id)
        dept = self.get_single_dep(dep.dep_id)
        if dept:
            return 'Department already exist'
        else:
            db.session.add(dep)
            db.session.commit()
            return 'Department added successfully'
        if type(dep)==list:
            db.session.add_all(dep)
            db.session.commit()
            return 'Departments added successfully'

    def updat_dep(self,dep):
        dept = self.get_single_dep(dep.dep_id)
        if dept:
            dept.dep_name=dep.dep_name
            dept.dep_strength=dep.dep_strength
            dept.active='Y'
            db.session.commit()
            return 'department updated succsessfully'
        else:
            return 'Department does not exist'




    def delete_dep(self,dep_id):
        dept = self.get_single_dep(dep_id)
        if dept:
            dept.active='N'
            db.session.commit()
            return 'Department deleted succesfully'
        else:
            return 'Department doesnt exist'


    def get_all_deps(self):
        depts=Department.query.all()
        return depts


class StudDaoimpl(StudService):

    def add_stud(self, stud):
            studnt = self.get_single_stud(stud.id)
            if studnt:
                return 'Student already exist'
            else:
                db.session.add(stud)
                db.session.commit()
                return 'Student added successfully'

    def updat_stud(self, stud):
        std = self.get_single_stud(stud.id)
        if std:
            std.name = stud.name
            std.marks = stud.marks
            std.depId=stud.depId
            std.Active='Y'
            db.session.commit()
            return 'department updated succsessfully'
        else:
            return 'Department does not exist'

    def delete_stud(self, stud_id):
        stud = self.get_single_stud(stud_id)
        if stud:
            stud.Active = 'N'
            db.session.commit()
            return 'Student deleted succesfully'
        else:
            return 'Stiudent doesnt exist'

    def get_single_stud(self, stud_id):
        std = Student.query.filter_by(id=stud_id).first()
        if std:
            return std

    def get_all_studs(self):
        studs=Student.query.all()
        return studs