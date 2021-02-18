class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def numdata(cls, data):
        data = map(int, data)
        d, m, y = data
        return cls(d, m, y)

    @staticmethod
    def check(obj):
        if obj.month not in range(1, 13) or obj.day not in range(1, 32) or obj.year not in range(1970, 2100):
            return "в месяце не больше 31 дня, месяцев не больше 12, а года от 1970 до 2099. Поправьте если у вас не так"
        else:
            return f"{obj.day} {obj.month} {obj.year}"


x = input('введите дату в формате dd-mm-yyyy: ').split("-")

set_day = Date.numdata(x)
print(Date.check(set_day))

