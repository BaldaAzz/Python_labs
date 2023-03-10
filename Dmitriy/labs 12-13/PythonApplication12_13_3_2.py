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
    
    def write_info(self):
        count = int(input("Введите количесвто зданий:"))
        it = 0
        self.bildings = []
        
        while it < count:
            self.height = int(input("Введите высоту здания:")) 
            self.floor = int(input("Введите количевство этажей:")) 
            self.apartments = int(input("Введите колчичевство квартир:")) 
            self.entrances = int(input("Введите колчичевство подъездов:")) 
            lst = [self.height, self.floor, self.apartments, self.entrances,self.floor_height(), self.number_of_apartments_per_enterences(), self.number_of_apartments_per_floor(), self.randomize(), it]
            it += 1
            self.bildings.append(lst)
        return(self.bildings)
    
    
    def give_information(self):
        for i in self.bildings:
            print("номер здания:", i[-1] + 1, "высота здания:", i[0], "колличевстов этажей:", i[1], "количевстов квартир:", i[2], "колличевство подъездов:", i[3], "\nвысота этажа:", i[4], "квартир в подъезде:", i[5], "квартир на этаже:", i[6],"уникальный номер:", i[6], "\n") 
        
house = Buldings(None, None, None, None, None)
house.write_info()
house.give_information()
