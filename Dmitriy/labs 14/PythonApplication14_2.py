import random

class Vegetable:
    states ={1:'Отсутствует', 2:'Цветение',  3:'Зеленый', 4: 'Красный'}
    

    def __init__(self, _index):
        self._index = _index
        self._state = 1

    def grow(self):
        if self._state < 4:
            self._state + 1

    def is_ripe(self):
        if self._state == 4:
            print('Овощ созрел')
        else:
            print('Овощь не созрел')

class Tomato(Vegetable):

    def __init__(self,variety):
        self.variety = variety

    def give_variety(self):
        print('Список сортов:', self.variety)

class TomatoBush(Tomato):

    varieties = ['Агата', 'Де Барао', 'Бычье сердце', 'Сливка']
    a = random.choice(varieties)

    def __init__(self, number_of_tomatoes, variety):
        self.number_of_tomatoes = number_of_tomatoes
        self.variety = variety
        self.tomatoes = []
        
    def making_tomatoes(self):
        for tomato in range(0,self.number_of_tomatoes):
            tomato = Tomato(self.variety)
            self.tomatoes.append(tomato)
    
    def grow_all(self):
        for tomato in self.tomatoes:
            self.grow(tomato)
            

    def all_are_ripe(self):
        return [all (self.is_ripe)]

    def give_away_all(self):
        self.tomatoes = []
        
class Gardener(TomatoBush):
    def __init__(self,name,plant):
        self._plant = plant

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
print("0 - Агата \n1 - Де Барао\n2 - Бычье сердце\n3 - Сливка")
variety = int(input())
oneTomato = Tomato(TomatoBush.varieties[variety])
count = int(input("Введите количевство помидоров"))
bush = TomatoBush(count,oneTomato,)


Ivan = Gardener('Ваня', oneTomato)
print("Помогите нашему содовнику, Ване, собрать помидоры")
func = [print(Ivan.knowledge_base()),print(Ivan.work()),print(Ivan.harvest()),"Вы отлично справились"]
print("0 - подсказка\n1 - ростить\n2 - состояние\n3 - выход")
action = 0
while action != 3:
    action = int(input("введите действие:"))
    func[action]
    print(func[action])
