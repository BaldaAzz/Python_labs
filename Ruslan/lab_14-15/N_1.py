from random import choice


class Vegetable:
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')


    def __init__(self, _index, _state=states[0]):
        self._index = _index
        self._state = _state

    def grow(self):                                 # Проверяет статус зрелости и изменяет его
        if self._state == self.states[0]:
            self._state = self.states[1]

        elif self._state == self.states[1]:
            self._state = self.states[2]

        elif self._state == self.states[2]:
            self._state = self.states[3]

    def is_ripe(self):
            return self._state == self.states[3]    # Возвращает True, если созрел, и False, если нет



# Tomato = Vegetable(0)
# print(Tomato.is_ripe())
# for i in range(3):
#     Tomato.grow() 
#     print(Tomato.is_ripe())


class Tomato(Vegetable):

    def __init__(self, _index, variety, _state='Отсутствует'):
        super().__init__(_index, _state)
        self.variety = variety

    def grow(self):
       super().grow()
    
    def is_ripe(self):
       return super().is_ripe()

    def give_variety(self):                               # Возвращает информацию о сорте
        return self.variety


tomato = Tomato(0, 'Sort//')
print(tomato.is_ripe())
for i in range(3):
    tomato.grow() 
    print(tomato.is_ripe())
print(tomato.give_variety())


class TomatoBush:
    varieties = ('Агата', 'Де Барао', 'Бычье сердце', 'Сливка')

    def __init__(self, amount, variety=choice(varieties)):          # variety=choice(varieties)
        self.amount = amount                                        # Выбирает случайный сорт томата
        self.variety = variety
    
