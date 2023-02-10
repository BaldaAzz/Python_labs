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

    def give_variety(self):
        return self.variety



class TomatoBush(Tomato):
    varieties = ('Агата', 'Де Барао', 'Бычье сердце', 'Сливка')
    variety = varieties[randint(0,3)]
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')
    
    def __init__(self, tomatos_value=randint(1,5), variety=choice(varieties)):
        self.tomatos_value = tomatos_value
        self.variety = variety
        self.tomatos = ([Tomato(i, self.variety, self._state) for i in range(self.tomatos_value)])
        print(self.tomatos)


    def grow_all(self):
      [i.grow() for i in self.tomatoes] 

        
    
    def all_are_ripe(self):
        result = True
        for i in self.tomatoes:
            if not i.is_ripe():            # Метод is_ripe() возвращает True, если помидор созрел,
                result = False             # и False, если нет       
        return result
    
    def give_away_all(self):
        if TomatoBush.all_art_ripe(self):
            return self.tomatoes


class Gardener(TomatoBush):
    
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        self.basket = []
        
    def work(self):
        self._plant.grow_all()
    
    def harvest(self):
        tomatoes = self._plant.give_away_all()
        if tomatoes:
            print('Урожай успешно собран!')
            self.basket = tomatoes
        else:
            print('Урожай не дозрел!'))
            
    def get_variety_info(self):
        print('Сорт томата:', self.basket[0].give_variety())
    
    def knowledge_base():
        print('Harvest time for tomatoes should ideally occur\n'
            'when the fruit is a mature green and\n'
            'then allowed to ripen off the vine.\n'
            'This prevents splitting or bruising\n'
            'and allows for a measure of control over the ripening process.\n'
              )    
 
key = ...
while key != 0:
    key = int(input('Key: '))
    if key == 1:
        Gardener.knowledge_base()  
        '''Work'''
    if key == 2:
        t_b = TomatoBush()
        gardener = Gardener('Tom', t_b)
        '''Work'''
    if key == 3:
        gardener.work()
    if key == 4:
        gardener.harvest()
    if key == 5:
        gardener.work()
    if key == 6:
        gardener.harvest()
    if key == 7:
        gardener.give_variety_info()
