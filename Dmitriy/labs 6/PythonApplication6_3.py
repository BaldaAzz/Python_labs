n_strok = 5
m_stolb = 6
lst = [[int((n + 1) * (elem + 1)) for elem in range(n_strok)] for n in range(m_stolb)]

for i in range (len (lst)):
    print(*lst[i] , sep = " ")

