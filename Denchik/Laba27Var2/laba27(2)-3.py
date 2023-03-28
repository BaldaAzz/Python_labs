import pandas as pd

#Создайте табличную структуру данных.
tab = pd.DataFrame({
    'Наименования':["Грепфрут","Абрикос","Морковь","Нектарин","Баклажан","Грейпфрут","Лук","Персик","Морковь"],
    'Месяц':["Январь"]*9,
    'День':[1, 1, 1, 1, 1, 2, 2, 2, 2],
    'Склад':["#001", "#002", "#001", "#002", "#001", "#001", "#002", "#001", "#002"],
    'Продано':[0.00, 0.00, 741.83, 514.19, 1_213.81, 311.85, 207.90, 720.58, 110.46],
    'Менеджер':["Дубинин","Дубинин","Дубинин","Дубинин","Иванов","Михайлов","Дубинин","Иванов","Петров"],
    'Заказчик':["Орион","Али","Ланит","Звезда","Ланит","Шангри-Ла","Метелица","Тандем","Тандем"]},
    index=[1, 2, 3, 4, 5, 6, 7, 8, 9]  
    )

print(tab,'\n')

# Выведите название столбцов и данные таблицы отдельно.

print(tab.columns,'\n')
print(tab.rolling,'\n')

# Выведите значениястолбца Наименование.
print(tab['Наименования'],'\n')

# Затем выведите последовательно Месяц, День и Склад.
print(tab['Месяц'],'\n',tab['День'],'\n',tab['Склад'],'\n')
