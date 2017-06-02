class Colonel():
	def __init__(self,surname,countOfBattles,countOfVictories):
		self.surname=surname
		self.countOfBattles=countOfBattles
		self.countOfVictories=countOfVictories

	def Quality(self):

		q1 = ((self.countOfVictories)**2)/(self.countOfVictories)
		print('Качество ', q1)

	def Form_Info(self):
		print('Фамилия полководца ', self.surname)
		print('Количество битв ', self.countOfBattles)
		print('Количество побед ', self.countOfVictories)

class InheritedColonel(Colonel):
	def __init__(self,surname,countOfBattles,countOfVictories,p):
		super().__init__(surname,countOfBattles,countOfVictories)
		self.p=p
	def Quality(self):
		q2 = (self.p**2)/self.countOfBattles+((self.countOfVictories)**2)/(self.countOfVictories)
		print('Качество', q2)

colonel1 = Colonel('Иванов',5,4)
colonel2 = Colonel('Петров',8,5)
colonel3 = InheritedColonel('Кузнецов',6,5,2)
colonel4 = InheritedColonel('Дмитриев',7,4,3)

colonel1.Form_Info()
colonel1.Quality()

colonel2.Form_Info()
colonel2.Quality()

colonel3.Form_Info()
colonel3.Quality()

colonel4.Form_Info()
colonel4.Quality()