from itertools import cycle

# print('тут надо будет ввести целое число от 0 до 9.') ## тут получается первая часть задачи
# for el in count(int(input('введите целое цисло:'))):
#     print(el)
#     if el == 10:
#         break

print('тут надо вводить список, а его программа повторит. для продолжения нажмите Enter для выхода - введите q')
my_list = input('введите элементы списка чесрез пробел ').split() ## а это вторая часть
for el in cycle(my_list):
    print(el, end='')
    ending = input()
    if ending == 'q':
        break
