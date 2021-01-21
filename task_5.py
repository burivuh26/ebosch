rating = [10, 8, 6, 5, 5, 4, 2, 1]
num = int(input('введите натуральное число: '))
i = 0
for f in rating:
    if num <= f:
        i += 1
rating.insert(i, num)
print(rating)
