task_list = input("введите числа через пробел: ").split()
for idx in range(1, len(task_list), 2):
    task_list.insert(idx - 1, task_list.pop(idx))

print(task_list)
