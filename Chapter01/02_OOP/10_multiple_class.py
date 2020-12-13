class Worker:
	def coffee(self):
		print("커피 마시기")

class Designer(Worker):
	def design(self):
		print('새 캐릭터 창작')
		
class Programmer(Worker):
	def newapp(self):
		print('새 앱 개발')
		
class Owner(Designer, Programmer):
	def lunch(self):
		print("작업 후 점심 식사")
		
owner1 = Owner()
owner1.coffee()
owner1.design()
owner1.newapp()
owner1.lunch()
