class Stationery:
    def __init__(self, title):
        self.title = title
        print(title)

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой, медленно и печально')


class Pencile(Stationery):
    def draw(self):
        print('Рисуем карандашом, ну эт конечно повеселее уже')


class Handle(Stationery):
    def draw(self):
        print('Опа, а маркером рисовать-то отлично!')


pen_draw = Pen('Рисуем ручкой!!!')
pen_draw.draw()
print()
pencile_draw = Pencile("Рисуем карандашом!!!")
pencile_draw.draw()
print()
handle_draw = Handle('Рисуем маркером!!!')
handle_draw.draw()
