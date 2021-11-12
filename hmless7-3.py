class Spor:
    def __init__(self, numbers):
        self.numbers = numbers

    def make_order(self, rows):
        return '\n'.join(['O' * rows for _ in range(self.numbers // rows)]) + "\n" + 'O' * (self.numbers % rows)

    def __str__(self):
        return f'{self.numbers}'

    def __add__(self, other):
        print('Сумма ячеек равна:')
        return Spor(self.numbers + other.numbers)

    def __sub__(self, other):
        print('Вычитаниие из ячейки:')
        return Spor(self.numbers - other.numbers) if self.numbers - other.numbers > 0 \
            else "Количество ячеек не позволяет вичитать, так как в первой меньше чем во второй"

    def __mul__(self, other):
        print('Умножение клеток:')
        return Spor(self.numbers * other.numbers)

    def __floordiv__(self, other):
        print('Деление:')
        return Spor(self.numbers // other.numbers)


spor_1 = Spor(36)
spor_2 = Spor(18)
print(spor_1 + spor_2)
print(spor_1 - spor_2)
print(spor_1 * spor_2)
print(spor_1 // spor_2)
print(spor_2.make_order(5))
