class Vegetable:
    stages = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index, stage=stages[0]):
        self.index = index
        self.stage = stage
    
    def grow(self):
        if self.stage == self.stages[0]:
            self.stage = self.stages[1]

        elif self.stage == self.stages[1]:
            self.stage = self.stages[2]

        elif self.stage == self.stages[2]:
            self.stage = self.stages[3] 
    
    def is_ripe(self):
            return self.stage == self.stages[3]



# Tomato = Vegetable(0)
# print(Tomato.is_ripe())
# for i in range(3):
#     Tomato.grow() 
#     print(Tomato.is_ripe())


class Tomato(Vegetable):

    def __init__(self, index, sort, stage='Отсутствует'):
        super().__init__(index, stage)
        self.sort = sort

    def grow(self):
       return super().grow()
    
    def is_ripe(self):
       return super().is_ripe()

    def get_sort_info(self):
        return self.sort


tomato = Tomato(0, 'Sort//')
print(tomato.is_ripe())
for i in range(3):
    tomato.grow() 
    print(tomato.is_ripe())
print(tomato.get_sort_info)