from  random import randint

class Buldings():
    
    def __init__(self,height,floor,number,apartments,entrances):
        self.height = height
        self.floor = floor
        self.number = number 
        self.apartments = apartments
        self.entrances = entrances
      
    def floor_height (self):
        return (self.height / self.floor)

    def number_of_apartments_per_enterences(self):
        return(self.apartments // self.entrances)
        
    def number_of_apartments_per_floor(self):
        return(self.apartments // self.floor)

    def randomize(self):
        return(randint(1,1000))
    
    def write(self):
        self.height = int(input("Введите высоту здания:")) 
        self.floor = int(input("Введите количевство этажей:")) 
        self.apartments = int(input("Введите колчичевство квартир:")) 
        self.entrances = int(input("Введите колчичевство подъездов:")) 
    
    def give_information(self):
        print("высота здания:",self.height,"колличевстов этажей:",self.floor,"количевстов квартир:",self.apartments,"колличевство подъездов:",self.entrances) 
        
house = Buldings(None,None,None,None,None)
count = int(input("Введите количесвто зданий:"))
it = 0

while it < count:
    house.write()
    print(house.give_information())
    print("высота этажа:",house.floor_height(),"метра")
    print("колличевcтво квартир в подъезде",house.number_of_apartments_per_enterences())
    print("колличевство квартир на этаже:",house.number_of_apartments_per_floor())
    print("случайный номер:",house.randomize())
    it += 1
    