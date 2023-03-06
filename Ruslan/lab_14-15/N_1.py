from random import choice, randint


class Vegetable:
    def __init__(self, _index):
        self._index = _index
        self.states = {0: 'Отсутствует',
                       1: 'Цветение',
                       2: 'Зеленый', 
                       3: 'Красный'}
        self._state = self.states[0]
        self._state_x = 0


    def grow(self):                                 # Проверяет статус зрелости и изменяет его
        if self._state_x == len(self.states.keys()) - 1:
            pass
        else:
            self._state_x += 1
            self._state = self.states[self._state_x]

    def is_ripe(self):
            return self._state == self.states[3]    # Возвращает True, если созрел, и False, если нет



# Tomato = Vegetable(0)                             # Проверка класса
# print(Tomato.is_ripe())
# for i in range(3):
#     Tomato.grow() 
#     print(Tomato.is_ripe())


class Tomato(Vegetable):

    def __init__(self, _index, variety):
        super().__init__(_index)
        self.variety = variety


    def give_variety(self):                               # Возвращает информацию о сорте
        return self.variety


# tomato = Tomato(0, 'Агата')                             # Проверка класса
# print(tomato.is_ripe())               
# for i in range(3):
#     tomato.grow() 
#     print(tomato.is_ripe())
# print(tomato.give_variety())


class TomatoBush:
    varieties = ('Агата', 'Де Барао', 'Бычье сердце', 'Сливка')

    def __init__(self, number_of_tomatoes=randint(1, 10), variety=choice(varieties)):          # variety=choice(varieties)
        self.number_of_tomatoes = number_of_tomatoes                                        # Выбирает случайный сорт томата
        self.variety = variety
        self.tomatoes = [Tomato(i, self.variety) for i in range(self.number_of_tomatoes)]


    def grow_all(self):                     # Рост томатов
        for i in self.tomatoes:
            i.grow()


    def all_are_ripe(self):
        result = True
        for i in self.tomatoes:
            if not i.is_ripe():            # Метод is_ripe() возвращает True, если помидор созрел,
                result = False             # и False, если нет       
        return result


    def give_away_all(self):                    # Сбор урожая
        if TomatoBush.all_are_ripe(self):
            return self.tomatoes



# bush = TomatoBush(15)                             # Проверка класса
# print(bush.all_are_ripe())
# for i in range(3):
#     bush.grow_all()
# print(bush.all_are_ripe())
# print(bush.give_away_all())


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        self.basket = []


    def work(self):                                                 # Ухаживание за растением
        self._plant.grow_all()


    def harvest(self):                                              # Сбор урожая
        tomatoes = self._plant.give_away_all()
        if tomatoes:
            print('Урожай успешно собран!')
            self.basket = tomatoes
        else:
            print('Урожай не дозрел!')
        

    def get_variety_info(self):
        print('Сорт томата:', self.basket[0].give_variety())

    def knowledge_base(self):
        print('''
Чтобы томаты созрели, за ними нужно ухаживать(work())
Когда томаты созрели, их нужно собрать(harvest())
Посмотреть, чтобы узнать сорт собранных томатов(get_variety_info())''')




# Тест программы 
tb = TomatoBush()
gardener = Gardener('Принц Чарльз Кинг Чихуахуа', tb)
gardener.knowledge_base()
gardener.harvest()
for i in range(3):
    gardener.work()
gardener.harvest()
gardener.get_variety_info()
