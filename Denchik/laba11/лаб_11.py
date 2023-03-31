
class Numbers:
    def __init__(self, *nums):
        self.nums = nums
        self.k = k

    def average_numbers(self,*nums):
        print('Среднее арифмитическое: ', sum(nums) / len.nums)

    def max_number(self):
        for s in a,b,c,d:
            if s > self.k:
                self.k = s
        print('Наибольшее: ',self.k)
        
k = 0
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
counter = Numbers(a, b, c, d, k)
counter.average_numbers()
counter.max_number()
