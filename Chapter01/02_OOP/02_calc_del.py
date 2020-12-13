class Calculator: 
    def __init__(self): 
        self.result = 0 

    def __del__(self): 
        print("Calculator object is deleted")

cal1 = Calculator()
del cal1
