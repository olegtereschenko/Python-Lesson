from random import choice

class Car:
    """" Main car """
    direction = ['N','NE','E','SE','S','SW','W','NW']

    def __init__(self,name,color,speed,police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.police = police
        print(f'Машина:{name} цвета:{color}.\nЭто машина полиции?{police}')

    def go(self):
        print(f'{self.name}: Машина двигается!')

    def stop(self):
        print(f'{self.name}: Машина остановилась!')

    def turn(self):
        print(f'{self.name}: Машина повернула {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Скорость машины: {self.speed}'

class TownCar(Car):
    """CITYCAR"""
    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Ускорение!:'if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    """TRUCK"""
    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}. Ускорение!:'if self.speed > 40 else super().show_speed()

class SportCar(Car):
    """SPORTCAR"""

class PoliceCar(Car):
    """Police"""
    def __init__(self,name,color,speed,police=True):
        super().__init__(name,color,speed,police=True)

police_car = PoliceCar('ЛАДА','синий',100)
work_car = WorkCar('Газель','немытая',40)
sport_car = SportCar('Ламба','красный',130)
town_car = TownCar('Ока','белый',65)

list_of_cars = [police_car,work_car,sport_car,town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
