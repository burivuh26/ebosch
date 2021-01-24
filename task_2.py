def data(**kwargs):
    return ' '.join(kwargs.values())


print(data(name=input('введите имя: '), surname=input('введите фамилию: '), email=input('введите email: '),
           yearBirth=input('введите год рождения: '), city=input('введите город проживания: ')))
