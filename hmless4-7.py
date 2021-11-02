def gener(number):
    number_1 = 1

    for i in range(number + 1):
        yield f'{i}!={number_1}'
        number_1 *= i + 1


for el in gener(int(input('Число факториал'))):
    print(el)
