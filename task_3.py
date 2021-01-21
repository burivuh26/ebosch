# -----------------------вариант решения 1 костыльный, аж самому стыдно


# number = int(input('введите номер месяца: '))
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if number in months[:2]:
    print(f'{number}-месяц - зима')
elif number in months[2:5]:
    print(f'{number}-месяц - весна')
elif number in months[5:8]:
    print(f'{number}-месяц - лето')
elif number in months[8:11]:
    print(f'{number}-месяц - осень')
elif number == 12:
    print(f'{number}-месяц - зима')


# ------------------------------ вариант 2 ------------------------------
number = int(input('введите номер месяца: '))
months_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
               9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
print(f'{number}-й месяц года — это {months_dict.get(number)}')
