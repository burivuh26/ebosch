with open(r"/Users/burivuh26/PycharmProjects/pythonProject/text.txt", "w") as file:
    while True:
        line = input('введите текст: ')
        if not line:
            break
        file.write(line + '\n')
