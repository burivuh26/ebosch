revenue = int(input('введите выручку вашей фирмы: '))
costs = int(input('ввелите издержки фирмы: '))
profit = revenue - costs
if profit < 0:
    print('ваша фирма убыточна. Нужно срочно что-то с этим делать')
elif profit == 0:
    print('вы вышли в 0! уже неплохо, но нужно больше')
elif profit > 0:
    profitability = profit / revenue
    people = int(input('введите клдичество ваших сотрудников: '))
    print(f'ваша фирма прибыльна! рентабельность: {profitability}. Прибыль на каждого сотрудника составляет:',
          profit / people)
