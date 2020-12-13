class Ex:
    def __init__(self):
        self.pub = "I'm public"
        self.__pri = "I'm private"

ex = Ex()
print(ex.pub)
print(ex.pri)
