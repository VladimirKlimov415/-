class KineticEnergy:
	
	def __init__(self,mass,velocity):
		
		self.mass=mass
		self.velocity=velocity

	def FormString(self):
		m=str(self.mass)
		v=str(self.velocity)
		info='Масса: '+m+' Скорость: '+v
		print(info)


	def Energy(self):
		w=(self.mass*self.velocity*self.velocity)/2
		print('Кинетическая энергия: ', w)


m=int(input('Введите массу: '))
v=int(input('Введите скорость: '))

body=KineticEnergy(m,v)
body.FormString()
body.Energy()


	



		