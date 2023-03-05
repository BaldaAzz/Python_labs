from datetime import datetime

year = datetime.today().year
day = 365

class Worker():
    def __init__(self, surname, salary, year_work, count):
        self.surname = surname
        self.salary = salary
        self.year_work = year_work 
        self.count = count

    def number_of_years(self):
        return(year - self.year_work)

    def number_of_days(self):
        return((self.number_of_years() - 1) * day )
          
    def write_info(self):
        it = 0
        self.lst_workers = []
        
        while it < self.count:
            self.surname = str(input("Введите фамилию:"))
            self.salary = int(input("Введите заработную плату:"))
            self.year_work = int(input("Введите год с которого начали работать:"))
            lst = [self.surname, self.salary, self.year_work, self.number_of_days(), self.number_of_years()] 
            self.lst_workers.append(lst)
            it += 1
        return self.lst_workers
    
    def info(self):
        for i in self.lst_workers:
            print("\nФамилия:", i[0], "\nзарабатная плата:", i[1], "\nначал работать:", i[2], "\nстаж работы:", i[3], "дней", "\nсотрудник отработал", i[4], "лет")       
        
count = int(input("Введите колисчевсто сотрудников:"))

worker = Worker(None, None, None, count)
worker.write_info()
worker.info()
 