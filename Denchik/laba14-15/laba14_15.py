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

    def is_ripe(self):
            return self._state == self.states[3]    #Возвращает True, если созрел, и False, если нет


class Tomato(Vegetable):
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, _index, variety,  _state=states[0]):
        super().__init__(_index, _state)
        self.variety = variety

    def grow():
        super().grow()

    def is_ripe(self):
        return super().is_ripe()

    def give_variety(self):
        return self.variety



class TomatoBush(Tomato):
    varieties = ('Агата', 'Де Барао', 'Бычье сердце', 'Сливка')
    i = randint(0,4)
    variety = varieties[i]
    print(variety)


    def __init__(self, tomatos):
        self.tomatos = tomatos

    
    def make_bush(self):
        self.tomatos = [Tomato(i, self.variety) for i in range(self.tomatos)]
    
    def grow_all(self):
        for i in self.tomatos:
            super().grow()
    
    def all_are_ripe(self):
        if all(self.tomatos.is_ripe()):
            return True
    
    def give_away_all(self):
        self.tomatos.clear()


class Gardener(TomatoBush):
    _plant = Tomato

    def __init__(self, name):
        self.name = name
    
    def work(self):
        super().grow()
    
    def harvest(self):
        if super().grow_all():
            super().give_away_all()
        else:
            print('Не все помидорки созрели!')
    
    def knowledge_base():
        print('''
        Чтобы собрать урожай, нужно посадить куст(make_bush())
        Чтобы помидорки выросли, нужно ухаживать за кустом(work())
        Для сбора урожая нужно harvest()
        ''')    
    
a=Vegetable(2)
Vegetable.grow
Gardener.knowledge_base