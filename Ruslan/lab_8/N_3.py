tegs_list = list(map(str, input().split()))
teg_count = len(tegs_list)
errors = set()

for i in tegs_list:
    i.lower()    
    if i[0] != "#":
        errors.add("Хештег начинается не с #")        
    if i == "#":
        errors.add("Хештег состоит только из #")       
    if i.find("#") != i.find("#"):
        errors.add("Хештеги не разделёны пробелом")
    if teg_count > 5:
        errors.add("Слишком много хештегов")
    if len(i) > 20:
        errors.add("Слишком длинный хештег")

    for j in range(len(tegs_list)):
            if i == tegs_list[j]:
                errors.add("Хештеги одинаковы")

for error in errors:
    print(error)