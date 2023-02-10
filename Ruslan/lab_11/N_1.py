class Worker:

    def __init__(self, lastname, post, salary):
        self.lastname = lastname
        self.post = post
        self.salary = salary
    
    def increase_salary(self):
        self.salary += self.salary * 0.15
    
    def assign_position(self):
        if 'Иван' in self.lastname:
            self.post = 'инженер'


names = {'Иван': [], 'Принц Чарльз Кинг Чихуахуа', 'Игорь', 'Tom'}
gardeners = []
for i in names:
    gardeners = [Worker()]
worker = Worker('Llls', 'adasd', 1526)
worker.increase_salary()
print(worker.salary)