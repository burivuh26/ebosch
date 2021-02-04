class Road:
    def __init__(self, length, width):
        mass = (length * width * 25 * 5) / 1000
        print(round(mass, 3))


road = Road(5000, 20)
