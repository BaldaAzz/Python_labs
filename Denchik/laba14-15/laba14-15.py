from random import randint, choice


class Vegetable:

    states = ('Absent', 'Flowering',    #'Отсутствует', 'Цветение',
              'Green', 'Red')         #'Зеленый', 'Красный'

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
        print(self, self._state)

    def is_ripe(self):
        return self._state == self.states[3]


class Tomato(Vegetable):
    states = ('Absent', 'Flowering',    #'Отсутствует', 'Цветение',
              'Green', 'Red')         #'Зеленый', 'Красный'
              

    def __init__(self, _index, variety,  _state=states[0]):
        super().__init__(_index, _state)
        self.variety = variety

    def give_variety(self):
        return self.variety


class TomatoBush(Tomato):
    varieties = ('Agata', 'De Barao',                  #Агата, Де Барао, 
                 'Bull heart', 'Cream')                #Бычье сердце, Сливка

    def __init__(self, tomatos_value=randint(1, 3), variety=choice(varieties)):
        self.tomatos_value = tomatos_value
        self.variety = variety
        self.tomatoes = ([Tomato(i, self.variety)
                         for i in range(self.tomatos_value)])

    def grow_all(self):
        [i.grow() for i in self.tomatoes]

    def all_are_ripe(self):
        result = True
        for i in self.tomatoes:
            if not i.is_ripe():
                result = False
        return result

    def give_away_all(self):
        if TomatoBush.all_are_ripe(self):
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
            print('the harvest has been successdully harvested!\n')
            self.basket = tomatoes
        else:
            print('The harvest isnt ripe!\n')

    def get_variety_info(self):
        if self.basket != []:
            print('Variety:',
                  self.basket[0].give_variety(), '\n')
        else:
            print('The harvest hasnt been harvested yet!\n')

    def knowledge_base():
        print('Harvest time for tomatoes should ideally occur\n'
              'when the fruit is a mature green and\n'
              'then allowed to ripen off the vine.\n'
              'This prevents splitting or bruising\n'
              'and allows for a measure of control over the ripening process.\n'
              )


key = ...
print('\n' * 10)
while key != 0:
    print('1. Knowledge base\n'
          '2. Create TomatoBush and Gardener\n'
          '3. Gardener work\n'
          '4. Gardener harvest\n'
          '5. Harvested Variety'
          )
    key = int(input('Key: '))
    if key == 1:
        print('\n' * 10)
        Gardener.knowledge_base()
    if key == 2:
        print('\n' * 10)
        t_b = TomatoBush()
        gardener = Gardener('Tom', t_b)
        print('Created:\n',t_b.tomatoes,
              '\n', gardener, '\n')
    if key == 3:
        print('\n' * 10)
        gardener.work()
        print('\n')
    if key == 4:
        print('\n' * 10)
        gardener.harvest()
    if key == 5:
        print('\n' * 10)
        gardener.get_variety_info()
