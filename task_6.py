a = float(input('сколько спортсмен бежит: '))
b = int(input('сколько ему надо бежать: '))
day = 1
while a < b:
    print(f'{day}-й день: {a:.3} км')
    a = a + (a * 0.1)
    day = day + 1
    continue
print(f'{day}-й день: {a:.3} км')
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
