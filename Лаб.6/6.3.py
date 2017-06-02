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

class PotentialEnergy(KineticEnergy):
    def __init__(self,mass,velocity,height):
        super().__init__(mass,velocity)
        self.height = height

    def CalculatePotentialEnergy(self):
        e = self.mass * self.height*9.8
        print('Потенциальная энергия: ', e)

m=int(input('Введите массу: '))
v=int(input('Введите скорость: '))
h=int(input('Введите высоту: '))

bodyParent = KineticEnergy(m,v)
bodyChild = PotentialEnergy(m,v,h)
 
bodyParent.FormString()
bodyParent.Energy()
bodyChild.CalculatePotentialEnergy()       