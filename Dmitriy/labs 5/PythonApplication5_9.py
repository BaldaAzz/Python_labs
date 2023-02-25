from random import randint

lst = [randint(1,5) for i in range(5)]
print(lst)

if lst == lst[::-1]:
    print("он симметричный")
else: 
    print("он не симметричный")




