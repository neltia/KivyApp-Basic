class Calculator: 
    def __init__(self): 
        self.result = 0 

    def add(self, num): 
        self.result += num 
        return self.result

cal1 = Calculator()
cal2 = Calculator() 

print(cal1.add(5))
print(cal1.add(2))
print(cal2.add(2))
print(cal2.add(8))
