teg = list(map(str, input("Ввод хештегов:").split()))
teg_count = teg.count(' ') + 1
errors = set()

for i in teg:
    i.upper()    
    if i[0] != "#":
        errors.add("Хештег начинается не с #")        
    if i == "#":
        errors.add("Хештег состоит только из #")       
    if i.find("#") != i.rfind("#"):
        errors.add("Хештеги не разделёны пробелом")
    if teg_count > 5:
        errors.add("Слишком много хештегов")
    if len(i) > 20:
        errors.add("Слишком длинный хештег")
    for j in range(len(teg)):
        teg[j] = teg[j].upper()
        for k in range(len(teg)):
            teg[k] = teg[k].upper()
            if j != k:
                if teg[j] == teg[k]:
                    errors.add("Хештеги равны")
for i in errors:
    print (i)
    