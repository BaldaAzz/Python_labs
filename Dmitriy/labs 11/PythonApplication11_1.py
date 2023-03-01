class Worker():
    
    def __init__(self,surname,salary,year_work):
        self.surname = surname
        self.salary = salary
        self.year_work = year_work 

    def number_of_years(self):
        return(2023 - self.year_work)

    def number_of_days(self):
        return((2023 - self.year_work - 1) * 365)
    
    def write_info(self):
        self.surname = str(input("Введите фамилию:"))
        self.salary = int(input("Введите заработную плату:"))
        self.year_work = int(input("Введите год с которого начали работать:"))
        return(self.surname,self.salary,self.year_work) 
      
    def info(self):
        print("\nФамилия:",self.surname,"\nзарабатная плата:", self.salary , "\nначал работать:",self.year_work)
        
worker = Worker(None,None,None)

count = int(input("Введите количество сотрудников:"))
it = 0

while it < count:
    worker.write_info()
    worker.info()
    print("работает",worker.number_of_years(),"лет")
    print("работает после года",worker.number_of_days(),"дней\n")
    it += 1
    