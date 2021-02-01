# list = []
# with open(r"/Users/burivuh26/PycharmProjects/pythonProject/text.txt", "r") as file:
#     for line in file:
#         list.append(line)
#
# lines = (len(list) + 1)
# print(f'всего {lines} строк') ## попытался решить с наскока и получилось посчитать только количество строк


with open(r"/Users/burivuh26/PycharmProjects/pythonProject/text.txt", "r") as file:
    line = file.readlines()
    for ind, value in enumerate(line, 1):
        words = len(value.split())
        print(
            f'в строке {ind} — {words} слов')  ## возможно при таком решении первый вариент с количеством строк
                                               ## не имеет смысла, но я оставлю. Файл используется, созданный в 1 задании.