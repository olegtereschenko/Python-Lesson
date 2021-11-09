class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit':wage, 'bonus':bonus}

class Position(Worker):
    def full_name(self):
        return f'{self.name} {self.surname}'

    def full_profit(self):
        return f'{sum(self._income.values())}'

manager = Position('Leo','Black','HR',130000,25000)
print(manager.full_name())
print(manager.full_profit())
print(manager.position)