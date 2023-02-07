
def copitalization(a, years, procent=0.1):
    years_copitalization = a
    while years != 0:
        years_copitalization += years_copitalization * procent
        years -= 1
    return print(years_copitalization) 
               
a = 1000
years = 5
copitalization(a, years)
