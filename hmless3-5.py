def summa():
    i = 0
    while True:
        onelist = input('Введите любые числа через пробел, введите "q" для выхода из програмы: ').split()
        for number in onelist:
            if number.lower() == "q":
                return i
            else:
                try:
                    i += int(number)
                except ValueError:
                    print('Для выхода из програмы введите - "q"')
        print(f"Сумма чисел = {i}")


print(summa())
