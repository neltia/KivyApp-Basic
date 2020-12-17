class Message:
    """Message 추상 클래스"""
    def __init__(self, data):
        self.data = data
        
    @staticmethod
    def is_collect_grade_message(data: dict):
        return False
 
class FirstGradeMessage(Message):
    """FirstGrade에 대한 메세지 처리 클래스"""
    @staticmethod
    def is_collect_grade_message(data: dict):
        return data['grade'] == 1
    
class SecondGradeMessage(Message):
    """SecondGrade에 대한 메세지 처리 클래스"""
    @staticmethod
    def is_collect_grade_message(data: dict):
        return data['grade'] == 2
    
class ThirdGradeMessage(Message):
    """ThirdGrade에 대한 메세지 처리 클래스"""
    @staticmethod
    def is_collect_grade_message(data: dict):
        return data['grade'] == 3
    
class DefaultGradeMessage(Message):
    """DefaultGrade에 대한 메세지 처리 클래스"""
    
class GradeMessageClassification():
    """Grade에 따른 메세지 분류 클래스"""
    def __init__(self, data):
        self.data = data
        
    def classification(self):
        for grade_message_cls in Message.__subclasses__():
            try:
                if grade_message_cls.is_collect_grade_message(self.data):
                    return grade_message_cls(self.data)
            except KeyError:
                continue
                
            return DefaultGradeMessage(self.data)


출처: https://doorbw.tistory.com/237 [Tigercow.Door]