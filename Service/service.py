import abc

class Service(metaclass=abc.ABCMeta):
    @classmethod
    def add(self):pass
    @classmethod
    def update(self):pass
    @classmethod
    def delete(self):pass
    @classmethod
    def check(self):pass