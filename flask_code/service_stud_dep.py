from abc import ABC,abstractmethod





class DepService(ABC):
    @abstractmethod
    def add_dep(self,dep):
        pass

    @abstractmethod
    def updat_dep(self,dep):
        pass

    @abstractmethod
    def delete_dep(self,dep_id):
        pass

    @abstractmethod
    def get_single_dep(self,dep_id):
        pass

    @abstractmethod
    def get_all_deps(self):
        pass


class StudService():
    @abstractmethod
    def add_stud(self, stud):
        pass

    @abstractmethod
    def updat_stud(self, stud):
        pass

    @abstractmethod
    def delete_stud(self, stud_id):
        pass

    @abstractmethod
    def get_single_stud(self, stud_id):
        pass

    @abstractmethod
    def get_all_studs(self):
        pass