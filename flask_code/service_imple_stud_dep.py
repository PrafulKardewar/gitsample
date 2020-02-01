from flask_code.dao_imple_stud_dep import *




depservice=DepDaoimple()
studservice=StudDaoimpl()

class DepServiceimple(DepService):

    @staticmethod
    def add_dep(dep):
        return depservice.add_dep(dep)

    @staticmethod
    def updat_dep(dep):
        return depservice.updat_dep(dep)

    @staticmethod
    def delete_dep(dep_id):
        return depservice.delete_dep(dep_id)

    @staticmethod
    def get_single_dep(dep_id):
        return depservice.get_single_dep(dep_id)

    @staticmethod
    def get_all_deps():
        return depservice.get_all_deps()

    @staticmethod
    def dummy_dep():
        return Department(dep_id='',dep_name='',dep_strength=0)


class StudServiceimpl():
    @staticmethod
    def add_stud(stud):
        return studservice.add_stud(stud)

    @staticmethod
    def updat_stud(stud):
        return studservice.updat_stud(stud)

    @staticmethod
    def delete_stud(stud_id):
        return studservice.delete_stud(stud_id)

    @staticmethod
    def get_single_stud(stud_id):
        return studservice.get_single_stud(stud_id)

    @staticmethod
    def get_all_studs():
        return studservice.get_all_studs()

    @staticmethod
    def dummy_stud():
        return Student(id='',name='',marks=0,depid='')