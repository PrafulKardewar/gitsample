from abc import ABC,abstractmethod




class Service(ABC):

    def add_dep(self,dep):
        pass

    def updat_dep(self,dep):
        pass

    def delete_dep(self,dep_id):
        pass