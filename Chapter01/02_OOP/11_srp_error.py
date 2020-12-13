class Person:
    """추상화 과정이 필요한 Person 클래스"""
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def choose_room(self):
    """숙소 방 정하기"""
    if(self.sex == '남자'):
        print("2층으로 간다.")
    elif(self.sex == '여자'):
        print("3층으로 간다.")
    else:
        print("성별을 지정해주세요.")
