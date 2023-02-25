lst = [1,7,5,4,78,45,31,15,3,6,7]
minimum=0
maximum=0

minimum = lst.index(min(lst))
maximum = lst.index(max(lst))

lst[minimum], lst[maximum] = lst[maximum], lst[minimum]
print(lst)
