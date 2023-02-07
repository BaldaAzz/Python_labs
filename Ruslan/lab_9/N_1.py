lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst)

def rearrange_list(list_nums, step):
    step %= len(list_nums)
    return list_nums[step::] + lst[:step:]

print(rearrange_list(lst, int(input())))