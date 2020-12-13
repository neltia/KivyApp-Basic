from abc import *

class personBase(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def choose_room(self):
        pass

class Male(personBase):
    def __init__(self, name):
        super().__init__(name)
        self.sex = "남자"
    def choose_room(self):
        print("2층으로 간다.")

class Female(personBase):
    def __init__(self, name):
        super().__init__(name)
        self.sex = "여자"
    def choose_room(self):
        print("3층으로 간다.")
