string = input("Введите слово: ")

if len(string) % 2 == 0:
    half_string1 = string[:len(string) // 2:]
    half_string2 = string[len(string) // 2::]
    print(half_string1, half_string2)
else:
    half_string1 = string[:len(string) // 2 + 1:]
    half_string2 = string[len(string) // 2 + 1::]
    print(half_string1, half_string2)