class designWorker:
	def __init__(self, name):
		self.name = name
	
	def work(self):
		print(self.name, ": 새로운 캐릭터를 창작하는 중")

class devWorker:
	def __init__(self, name):
		self.name = name
	
	def work(self):
		print(self.name, ": 새로운 앱을 개발하는 중")

employee1 = designWorker('Ann')
employee1.work()
employee2 = devWorker('Tom')
employee2.work()