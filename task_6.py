all = []
tovar = {'название': '', 'цена': '', 'количество': '', 'ед измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед измерения': []}
number = 0

while True:
    if input('Выход - Q, продолжение - Enter: ').upper() == 'Q':
        break
    number += 1
    tovar = tovar.copy()
    for f in tovar:
        pro = input('Введите данные товара: ')
        tovar[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(tovar[f])
    all.append((number, tovar))
    print(f'\nСтруктура товаров\n{all}')
    print(f'\nТекущая аналитика по товарам:\n {"#" * 29}')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
    print("#" * 30)
