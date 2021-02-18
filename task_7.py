class MyComplex:

    def __init__(self, re, im, *_):
        self.re = re
        self.im = im

    def __add__(self, other):
        return print(f'complex add = {self.re + other.re} + {self.im + other.im}j')

    def __mul__(self, other):
        return print(f'complex mul = {self.re * other.re - (self.im * other.im)} +'
                     f'{self.im * other.re + (self.re * other.im)}j')


a = MyComplex(4, 5)
b = MyComplex(6, 8)

c = a + b
d = a * b