list_words = input('введите несколько слов через пробел: ').split()
for ind, word in enumerate(list_words, 1):
    word = word.title()
    print(ind, word[:10])
