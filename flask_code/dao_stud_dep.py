from abc import ABC,abstractmethod




#crud
class DepService(ABC):

    def create_dep(self,dep):
        pass

    def updat_dep(self,dep):
        pass

    def delete_dep(self,dep_id):
        pass

    def get_single_dep(self,dep_id):
        pass

    def get_all_deps(self):
        pass


class StudService(ABC):

    def create_dep(self, dep):
        pass

    def updat_dep(self, dep):
        pass

    def delete_dep(self, dep_id):
        pass

    def get_single_dep(self, dep_id):
        pass

    def get_all_deps(self):
        pass