class Worker():
    def __init__(self,surname,position,salary):
        self.surname = surname
        self.position = position
        self.salary = salary
    
    def __del__(self):
        print('Объект удален')
    
    def rise_Salary(self):
        self.salary*=1.15
        print('Оклад '+self.surname+'a увеличен на 15% ')
        
    def set_Engineer(self):
        if self.surname.startswith ('Иван'):
            self.position = 'инженер'
            print(self.surname + '-инженер')
    def form_Info(self):
        print(str(self.surname) + ' имеет оклад ' + str(self.salary)+
           ' и должность '+ str(self.position))

class InheritedWorker(Worker):
    def __init__(self,surname,position,salary,rating):
        super().__init__(surname,position,salary)
        self.rating=rating

    def rise_Rating(self):
        if (self.rating>=60 and self.rating<=75):
            self.salary*=1.2
            print('Оклад '+str(self.surname)+'а увеличен на 20% ')
        elif (self.rating>75 and self.rating<=90):
            self.salary*=1.4
            print('Оклад '+str(self.surname)+'а увеличен на 40% ')
        elif (self.rating>90 and self.rating<=100):
            self.salary*=1.6
            print('Оклад '+str(self.surname)+'а увеличен на 60% ')

    def form_Info(self):
        print(str(self.surname) + ' имеет оклад ' + str(self.salary)+
           ' и должность '+ str(self.position) + ' рейтинг '+ str(self.rating))
        
workerA = Worker('Иванов','менеджер',50000)
workerB = Worker('Петров','кадровик',40000)
workerC = Worker('Сидоров','бухгалтер',45000)
workerD = InheritedWorker('Кузнецов','программист',60000,95)
workerE = InheritedWorker('Дмитриев','менеджер',70000,78)

workerA.form_Info()
workerB.form_Info()
workerC.form_Info()
workerD.form_Info()
workerE.form_Info()

workerA.rise_Salary()
workerB.rise_Salary()
workerC.rise_Salary()

workerD.rise_Rating()
workerE.rise_Rating()

workerA.set_Engineer()

workerA.form_Info()
workerB.form_Info()
workerC.form_Info()
workerD.form_Info()
workerE.form_Info()