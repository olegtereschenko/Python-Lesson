
class CNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __str__(self):
        return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'

    def __add__(self, other):
        return CNum(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return CNum((self.real * other.real - self.img * other.img),(self.img * other.real + self.real * other.img))


num_1 = CNum(3, -1)
num_2 = CNum(2, 7)
print(num_1 + num_2)
print(num_1 * num_2)
print(complex(3, -1) * complex(2, 7))