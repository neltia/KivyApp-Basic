class Person:
    def greeting(self):
        print('안녕하세요.')

class Teacher(Person):
    def teach(self):
        print('연습 문제를 풀어보세요.')

class Student(Person):
    def study(self):
        print('연습 문제 풀기.')
