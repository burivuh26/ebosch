class Division(Exception):
    def __init__(self, txt):
        self.txt = txt


del_big = int(input("введите делимое: "))
del_small = int(input("введите делитель: "))

try:
    if del_small == 0:
        raise Division("ай-ай-ай, на ноль делить нельзя")
except (Division) as err:
    print(err)
else:
    res = del_big / del_small
    print(res)
