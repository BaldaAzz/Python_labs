class Vegetable:
    key = 1
    states = {1: 'Отсутствует', 2: 'Цветение', 3: 'Зеленый', 4: 'Красный'}
    state = states[1]

    def __init__(self, index): 
        self.index = index
        self.state = self.states[1]

    def grow(self):
        if self.state != self.states[4]:
            self.state = self.states[self.key+1]
        else:
            self.state = Vegetable.states[4]
        self.key += 1
        return self.state

    def is_ripe(self):
        if self.state == self.states[4]:
            return 'Овощ созрел'
        else: 
            return 'Овощ не созрел'

    def get_info(self):
        print(self.state)

class Tomato(Vegetable):
    def __init__(self,variety):
        self.variety = variety

    def give_variety(self):
        return self.variety

class TomatoBush(Tomato):
    varieties = ['Агата', 'Де Барао', 'Бычье сердце', 'Сливка']

    def __init__(self, number_of_tomatoes, variety, key):
        self.number_of_tomatoes = number_of_tomatoes
        self.variety = variety
        self.tomatoes = []

        for tomato in range(0,self.number_of_tomatoes):
            tomato = Tomato(self.variety)
            self.tomatoes.append(tomato)
        

    def grow_all(self):
        if self.state != self.states[4]:
            self.state = self.states[self.key+1]
        else:
            self.state = Vegetable.states[4]
        self.key += 1
        return self.state

    def all_are_ripe(self):
        if self.state == self.states[4]:
            return True
        else:
            return False

    def give_away_all(self):
       self.tomatoes.clear()
       return self.tomatoes

    def get_list(self):
        print (self.tomatoes)

class Gardener(Vegetable):
    def __init__(self,name,plant):
        self.plant = plant

    def work(self):
        if self.state != self.states[4]:
            self.state = self.states[self.key+1]
        else:
            self.state = Vegetable.states[4]
        self.key += 1
        return self.state

    def harvest(self):
        harvested = []
        if self.state == self.states[4]:
            harvested.append(self.plant)
            print('\nТоматы созрели\n')
            return harvested
        else: print('\nНе все томаты созрели\n')

    def  knowledge_base(self):
        print("\nHarvest time for tomatoes should ideally occur \nwhen the fruit is a mature green and \nthen allowed to ripen off the vine.\nThis prevents splitting or bruising \nand allows for a measure of control over the ripening process")

pomidor = Vegetable(150)

bush = TomatoBush(29,"Бычье сердце",1)
bush.get_list()

oneTomato = Tomato('Де Барао')

Ivan = Gardener('Ваня', oneTomato)
Ivan.knowledge_base()
Ivan.work()
Ivan.harvest()
Ivan.work()
Ivan.work()
Ivan.harvest()
print(oneTomato.variety)
