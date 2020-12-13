class Ex:
    def __init__(self):
        self.pub = "I'm public"
        self.__pri = "I'm private"

    def print_pub(self):
        print(self.pub)

    def print_pri(self):
        print(self.__pri)

ex = Ex()
ex.print_pub()
ex.print_pri()