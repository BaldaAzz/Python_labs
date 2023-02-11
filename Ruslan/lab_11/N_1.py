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


names = {'Иван': ['зам. кого-то', 10000], 
         'Принц Чарльз Кинг Чихуахуа': ['инжинер', 125000],
         'Ярик': ['заведующий кладовой', 152], 
         'Tom': ['инжинер', 15640]}


workers = []
for name, value in names.items():
    workers.append(Worker(name, value[0], value[1]))

for i in workers:
    i.increase_salary()
    i.assign_position()

for i in workers:
    print(i.lastname, i.post, i.salary)