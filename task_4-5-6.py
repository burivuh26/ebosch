class Warehouse:
    def __init__(self, place, row):
        self.row = row # ряд на складе
        self.place = place # место в ряду

class Orgtech:
    def tech(self, format, connection): # формат - А4, А3 и тд. соединение - USB, Ethernet, wifi и тд.
        self.format = format
        self.connection = connection

class Scanner(Orgtech):
    def scan(self):
        pass

class Printe(Orgtech):
    def print(self):
        pass

class Xerox(Orgtech):
    def copy(self):
        pass


