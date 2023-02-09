''' 
1. Разобраться с взаимодействие (написать интерфейс)
2. Проверка вывода кода
3. Проверка с ТЗ
4. Исправление ошибок
'''



from random import randint


class Vegetable:

    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, _index, _state=states[0]):
        self._index = _index
        self._state = _state

    def grow(self):
        if self._state == self.states[0]:
            self._state = self.states[1]
        elif self._state == self.states[1]:
            self._state = self.states[2]
        elif self._state == self.states[2]:
            self._state = self.states[3]
        print(self , self._index ,self._state)
        
    def is_ripe(self):
            return print(self._state == self.states[3])  #Возвращает True, если созрел, и False, если нет


class Tomato(Vegetable):
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, _index, variety,  _state=states[0]):
        super().__init__(_index, _state)
        self.variety = variety
        
    def is_ripenow(self):
        print(super().is_ripe())

    def give_variety(self):
        return print(self.variety)



class TomatoBush(Tomato):
    varieties = ('Агата', 'Де Барао', 'Бычье сердце', 'Сливка')
    variety = varieties[randint(0,3)]
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')
    
    def __init__(self, tomatos_value, _state=states[0]):
        super().__init__(self.variety , _state)
        self.tomatos = ([Tomato(i, self.variety, self._state) for i in range(tomatos_value)])
        print(self.tomatos)


    def grow_all(self):
        super().grow()

        
    
    def all_are_ripe(self):
        if all((self.tomatos).is_ripe()):
            return True
    
    def give_away_all(self):
        self.tomatos.clear()


class Gardener(TomatoBush):
    _plant=Tomato
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')
    
    def __init__(self, name):
        self.name = name
        
    def work(self):
        super().grow_all()
    
    def harvest(self):
        if super().all_are_ripe():
            super().give_away_all()
        else:
            print('Не все помидорки созрели!')
    
    def knowledge_base():
        print('Harvest time for tomatoes should ideally occur\n'
            'when the fruit is a mature green and\n'
            'then allowed to ripen off the vine.\n'
            'This prevents splitting or bruising\n'
            'and allows for a measure of control over the ripening process.\n'
              )    
 
a = Vegetable('test')
d = Tomato
key = ...
while key != 0:
    key = int(input('Key: '))
    if key == 1:
        Gardener.knowledge_base()  
        '''Work'''
    if key == 2:
        b = TomatoBush(3)
        c = Gardener('Tom')
        '''Work'''
    if key == 3:
        a.grow()
        b.grow_all()
        b.is_ripenow()
        c.work()

    if key == 4:
        c.harvest()
    if key == 5:
        c.work()
    if key == 6:
        c.harvest()

    if key == 7:
        d.give_variety