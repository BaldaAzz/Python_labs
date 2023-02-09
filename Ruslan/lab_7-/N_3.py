from random import randint


# lst1 =[randint(0, 10) for i in range(randint(0, 10))]
# print(lst1)
# lst2 = [randint(0, 10) for i in range(randint(0, 10))]
# print(lst2)


# print(len(set(lst1).intersection(lst2)))
print(len(set([randint(0, 10) for i in range(randint(0, 10))]).intersection([randint(0, 10) for i in range(randint(0, 10))])))



