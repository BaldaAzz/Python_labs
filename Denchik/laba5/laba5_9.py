lst =input('Input with "," like (1,2,3,...): ')
lst = lst.split(',')


if lst == lst[::-1]:
    print('Symmetrical')
else:
    print('Unsymmetrical')