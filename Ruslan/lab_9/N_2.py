arr_in = [12, 23, 34, 45]
arr_out = []

def get_sum_num(number):
    sum_num = 0

    while number > 0:
        value = number % 10
        number //= 10

        sum_num += value
    return sum_num    


print([get_sum_num(num) for num in arr_in])
