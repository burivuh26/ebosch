def func(v1, v2):
    return v1 / v2


v1 = int(input('введите число: '))
v2 = int(input('введите число: '))

if v2 == 0:
    print('на 0 делить нельзя')
else:
    print(func(v1, v2))
