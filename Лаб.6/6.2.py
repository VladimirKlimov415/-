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

workerA = Worker('Иванов','менеджер',50000)
workerB = Worker('Петров','кадровик',40000)
workerC = Worker('Сидоров','бухгалтер',45000)

workerA.form_Info()
workerB.form_Info()
workerC.form_Info()

workerA.rise_Salary()
workerB.rise_Salary()
workerC.rise_Salary()

workerA.set_Engineer()

workerA.form_Info()
workerB.form_Info()
workerC.form_Info()

