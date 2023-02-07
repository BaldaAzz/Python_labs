file_input = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_5\employees.txt', 'r')
data = file_input.read()
file_input.close()

employees = []
employees_less_40 = []

for employee in data.split('\n'):
    employees.append(employee.split())

for employee in employees:
    if int(employee[1]) < 40:
        employees_less_40.append(employee)

file_employees_less_40 = open(r'C:\Users\Кардан\Desktop\Лабараторные\ИПО\1 семестр\lab_10\N_5\employees_less_40.txt', 'w')
for employee in employees_less_40:
    file_employees_less_40.write(' '.join(employee) + '\n')
file_employees_less_40.close()