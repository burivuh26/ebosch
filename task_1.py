from sys import argv

path, hours, rate, prize = argv
salary = ((float(hours) * float(rate)) + float(prize))
print(f'Зарплата сотрудника - {salary}')
