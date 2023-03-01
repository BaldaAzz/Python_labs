class Vegetable:
    states = {1:'Отсутствует', 2:'Цветение',  3:'Зеленый', 4: 'Красный'}

    def __init__(self, _index, _state = states[1]): 
        self._index = _index
        self._state = _state
        self.i = 0

    def grow(self):
        if self.i != len(self.states)-1:
            self.i += 1
            self._state = self.states[self.i]
        else: print('макимальная стадия')
        return(self._state)

    def is_ripe(self):
        if self._state == self.states[3]:
            return 'Овощ созрел'
        else: 
            return 'Овощ не созрел'

    def get_info(self):
        print(self._state)

class Tomato(Vegetable):
    def __init__(self,variety):
        self.variety = variety

    def give_variety(self):
        return self.variety

class TomatoBush(Tomato):
    varieties = ['Агата', 'Де Барао', 'Бычье сердце', 'Сливка']

    def __init__(self, number_of_tomatoes, variety):
        self.number_of_tomatoes = number_of_tomatoes
        self.variety = variety
        self.tomatoes = []

    def making_tomatoes(self):
        for tomato in range(0,self.number_of_tomatoes):
            tomato = Tomato(self.variety)
            self.tomatoes.append(tomato)
        
    def grow_all(self):
        [i.grow() for i in self.tomatoes]

    def all_are_ripe(self):
        if self._state == self.states[3]:
            return True
        else:
            return False

    def give_away_all(self):
       self.tomatoes.clear()
       return self.tomatoes

    def get_list(self):
        print (self.tomatoes)

class Gardener(TomatoBush):
    def __init__(self,name,plant):
        self.plant = plant

    def work(self):
        self.plant.grow_all()

    def harvest(self):
        harvested = []
        if self._state == self.states[3]:
            harvested.append(self.plant)
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
bush = TomatoBush(count,oneTomato)
bush.making_tomatoes()
bush.get_list()

Ivan = Gardener('Ваня', oneTomato)
print("Помогите нашему содовнику, Ване, собрать помидоры")
func = [Ivan.knowledge_base(),Ivan.work(),Ivan.harvest(),"Вы отлично справились"]
print("0 - подсказка\n1 - ростить\n2 - состояние\n3 - выход")
action = 0
while action != 3:
    action = int(input("введите действие:"))
    func[action]
    print(func[action])
