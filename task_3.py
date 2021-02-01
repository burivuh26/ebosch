with open(r"/Users/burivuh26/PycharmProjects/pythonProject/text_3.txt", "r") as file:
    workers = {line.split()[0]: float(line.split()[1]) for line in file}
    average_salary = sum(workers.values()) / len(workers)
    poor = [el[0] for el in workers.items() if el[1] < 20000]
    print(f'меньше 20 тысяч зарабатывают — {poor}\n'
          f'средняя зарплата вообще — {average_salary}')
