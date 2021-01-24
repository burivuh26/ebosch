def sum():
    number = 0
    while True:
        list = input('вводите числа, для выхода - Q: ').split()
        for item in list:
            if item == "Q":
                return number
            else:
                try:
                    number += int(item)
                except ValueError:
                    print('для выхода надо жать Q. Большое Q')
        print(f'сумма чисел - {number}')


print(sum())