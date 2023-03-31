
def sp(lst):
    for i in range(len(lst)):
        summa = 0
        while lst[i] > 0:
            summa += arr_in[i] % 10
            lst[i] //= 10
        arr_out.append(summa)
    return
    
arr_in = [127, 235, 343, 451]
arr_out = []

sp(arr_in)

print(arr_out)