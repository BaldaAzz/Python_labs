from random import randint
 
class Vegetable:
    states = {1:'Отсутствует', 2:'Цветение',  3:'Зеленый', 4: 'Красный'}

    def __init__(self, _index,): 
        self._index = _index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state + 1
        else: 
            print('макимальная стадия')
        return(self._state)

    def is_ripe(self):
        if self._state == self.states[3]:
            return 'Овощ созрел'
        else: 
            return 'Овощ не созрел'

class Tomato(Vegetable):
    def __init__(self,variety):
        self.variety = variety

    def give_variety(self):
        return self.variety

class TomatoBush(Tomato):
    varieties = ['Агата', 'Де Барао', 'Бычье сердце', 'Сливка']
    random_num = randint(0,3)

    def __init__(self, number_of_tomatoes, variety):
        self.number_of_tomatoes = number_of_tomatoes
        self.variety = variety
        self.tomatoes = []

    def making_tomatoes(self):
        for tomato in range(0,self.number_of_tomatoes):
            tomato = Tomato(self.variety)
            self.tomatoes.append(tomato)
        return self.tomatoes
        
    def grow_all(self):
        for tomato in self.tomatoes:
            self.grow(tomato)

    def all_are_ripe(self):
        if self._state == self.states[3]:
            return True
        else:
            return False

    def give_away_all(self):
       self.tomatoes.clear()
       return self.tomatoes

    def get_list(self):
        for tomat in self.tomatoes:
            print (tomat,TomatoBush.varieties[TomatoBush.random_num])

class Gardener(TomatoBush):
    def __init__(self,name,):
        self._plant = self.tomatoes

    def work(self):
        self.grow_all(self._plant)

    def harvest(self):
        harvested = []
        if self._state == self.states[3]:
            harvested.append(self._plant)
            return('\nТоматы созрели\n') and harvested
        else: return('\nНе все томаты созрели\n')

    def  knowledge_base(self):
        return("\nHarvest time for tomatoes should ideally occur \nwhen the fruit is a mature green and \nthen allowed to ripen off the vine.\nThis prevents splitting or bruising \nand allows for a measure of control over the ripening process")


index = int(input("введите индекс помидора:"))
pomidor = Vegetable(index)
print("введите вид помидора")
oneTomato = Tomato(TomatoBush.varieties[TomatoBush.random_num])
count = int(input("Введите количевство помидоров"))
bush = TomatoBush(count,oneTomato)
bush.making_tomatoes()
bush.get_list()
print(oneTomato)
Ivan = Gardener('Ваня')
Ivan.work()
