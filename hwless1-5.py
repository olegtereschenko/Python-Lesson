profit = int(input('Введите прибыль компании: '))
loss = int(input('Введите издержки компании: '))
a = profit - loss
if a > 0:
    print('Ваша компания работает с прибылью: ', a)
    b = float(profit/loss)
    print('Рентабельность вашей компании: ', b)
    if b > 0:
        staff = int(input('Введите число ваших сотрудников: '))
        salary = float(a / staff)
        print('Прибыль на одного сотрудника фирмы составляет: ', salary)
else:
    print('Рентабельность вашей компании равна нулю или убыточна :(')
