class MyEx(Exception):
    def __init__(self, txt):
        self.txt = txt


print('выполнение программы всегда можно остановить, введя "stop"')
my_list = []
while True:
    element = input('введите значение для списка: ')
    if element == 'stop':
        break
    try:
        if element.isdigit() == False:
            raise MyEx("в строку можно добавлять только числа")
    except (MyEx) as err:
        print(err)
    else:
        my_list.append(element)

print(my_list)
