class numItem: 
	def __init__(self, num): 
		self.Num = num

	def __add__(self, num):
		self.Num += num

n = numItem(45)
n + 100
print(n.Num)