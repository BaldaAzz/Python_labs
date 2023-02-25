arr_in = [12, 23, 34, 45]
arr_out = []

def summation_of_number(sam):
    summ = 0
    digit = 0
    
    while sam > 0:
        digit = sam % 10
        summ += digit
        sam //= 10
    return summ

for i in arr_in:
    arr_out.append(summation_of_number(i))

print("сумма числа:",arr_out)
