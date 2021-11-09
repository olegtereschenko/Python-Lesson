class Stationery:
    def __init__(self, title='Ну хоть чем-то рисуйте!'):
        self.title = title

    def draw(self):
        print(f'Начните рисовать!{self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title} ручкой!')

class Pencil(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title} карандашом!')

class Marker(Stationery):
    def draw(self):
        print(f'Начал рисовать {self.title} маркером!')

stat = Stationery()
pen = Pen('Гелевой')
pencil = Pencil('Очень твердым')
marker = Marker('Перманентным')

office_supplies = [stat,pen,pencil,marker]

for i in office_supplies:
    i.draw()