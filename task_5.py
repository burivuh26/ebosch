from functools import reduce

list = [el for el in range(100, 1001, 2)]
result = reduce(lambda x, y: x * y, list)
print(result)
