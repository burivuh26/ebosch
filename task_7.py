from math import factorial


def fact():
    n = int(input('введите число '))
    for i in range(1, n):
        list = [factorial(i)]
        yield list


for el in fact():
    print(el)
