
class Equipment:

    def __init__(self,model,color,paper,price):
        self._model = model
        self._color = color
        self._paper = paper
        self._price = price

    @property
    def model(self):
        return self._model


class Printer(Equipment):

    def __init__(self, model, color,paper,dpi):
        self.type = type
        super().__init__(model, color,paper,dpi)


class Copy(Equipment):

    def __init__(self, model, color, paper,dpi, printspeed, maxpaper):
        self.printspeed = printspeed
        self.maxpaper = maxpaper
        super().__init__(model, color, paper, dpi,printspeed, maxpaper)

class Scanner(Equipment):
    

    def add_Equipment(self, key, value):
        if self.__equipments.get(key) == None:
            self.__equipments[key] = 0
        self.__equipments[key] += value

    def issue_Equipment(self, key, value):
        rest = self.__equipments.get(key)
        if rest != None and rest >= value:
            self.__equipments[key] -= value
            if self.__equipments[key] == 0:
                del self.__equipments[key]

    def num(self, key):
        value = self.__equipments.get(key)
        return value if value != None else 0

    def equipments_in_warehouse(self):
        print('\n------------------------------------\nзапас на складе:\n------------------------------------')
        for i in self.__equipments:
            print(f'{models[i].model} - {self.num(i)} шт.')
        print('------------------------------------')

    def issued_equipments(self):
            print(f'\nIssued to office:\n{self.__equipments}') #что выдали

# список техники
# model, color, paper, dpi, printspeed, maxpaper
models = [Printer('Samsung EVO', 'color', 'A4', '500x500', '100', '1000 in day'),
          Printer('KYOCERA', 'color', 'A4-A3', '900x900', '150', '1500 in day'),
          Copy('HP', 'white-black', 'A4', '300x300', '120', '1200 in day'),
          Scanner('EPSON', 'color', 'A4-A1', '1200x1200', '180', '1800 in day')]

warehouse = Warehouse()
warehouse.equipments_in_warehouse()
#еще не дописал
