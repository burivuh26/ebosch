def int_func():
    for text in input('введите слова с пробелом из маленьких латинских букв: ').split():
        chars = 0
        for char in text:
            if 97 <= ord(char ) <= 122:
                chars += 1
        print(text.title())

int_func()
