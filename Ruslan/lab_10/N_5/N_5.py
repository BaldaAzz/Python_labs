data = ''
employees = []
employees_less_40 = []

with open('employees.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    for employee in data.split('\n'):
        employees.append(employee.split())

for employee in employees:
    if int(employee[1]) < 40:
        employees_less_40.append(employee)

with open('employees_less_40.txt', 'w', encoding='utf-8') as file:
    for employee in employees_less_40:
        file.write(' '.join(employee) + '\n')
