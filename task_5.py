with open("text_5.txt", "w") as file:
    numbers = input('введите числа через пробел: ').split()
    num_2 = []
    file.write(' '.join(numbers))
    for item in numbers:
        item = float(item)
        num_2.append(item)
    print(sum(num_2))
