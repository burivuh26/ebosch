class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'машина - {self.name}, цвет - {self.color}. Полицейская? {self.is_police}')

    def go(self):
        print(f'{self.name} машина поехала')

    def color(self):
        print(f'{self.color} - цвет машины')

    def stop(self):
        print(f'{self.name} машина остановилась')

    def turn(self, direction):
        print(f'{self.name} машина повернула {"направо" if direction == 1 else "налево"}')

    def show_speed(self, speed):
        print(f'{self.name} машина имеет скорость {self.speed}')


class TownCar(Car):
    def show_speed(self, speed):
        print(f'{self.name} машина имеет скорость {self.speed} {"Превышение!" if speed > 60 else ""}')


class WorkCar(Car):
    def show_speed(self, speed):
        print(f'{self.name} машина имеет скорость {self.speed} {"Превышение!" if speed > 40 else ""}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


ment = PoliceCar(120, 'белый', 'Мент')
ment.go()
ment.show_speed(120)
ment.turn(1)
ment.stop()
print()
sport = SportCar(250, 'зеленый', 'Lamborgini')
sport.go()
sport.show_speed(250)
sport.turn(0)
sport.stop()
print()
traktor = WorkCar(30, 'синий', 'Тр-Тр-Митя')
traktor.go()
traktor.show_speed(30)
traktor.turn(1)
traktor.stop()
print()
solaris = TownCar(80, 'черный', 'Солярис')
solaris.go()
solaris.show_speed(80)
solaris.turn(0)
solaris.stop()
