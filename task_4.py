num = int(input('введите целое положительное число: '))
max = 1
while num / 10 > 0:
    one = num % 10
    if one > max:
        max = one
    num = num // 10
print(max)
