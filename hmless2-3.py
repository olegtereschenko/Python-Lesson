month = int(input('Введите цифрой месяц согласно порядковому номеру в году и мы подскажем время года и сам месяц : '))
month_d = {1: 'Зима - Январь', 2: 'Зима - Февраль', 3: 'Весна - Март', 4: 'Весна - Апрель', 5: 'Весна - Май',
           6: 'Лето - Июнь', 7: 'Лето - Июль', 8: 'Лето - Август', 9: 'Осень - Сентябрь', 10: 'Осень - Октябрь',
           11: 'Осень - Ноябрь', 12: 'Зима - Декабрь'}
month_l = [' ', 'Зима - Январь', 'Зима - Февраль', 'Весна - Март', 'Весна - Апрель', 'Весна - Май', 'Лето - Июнь',
           'Лето - Июль', 'Лето - Август', 'Осень - Сентябрь', 'Осень - Октябрь', 'Осень - Ноябрь', 'Зима - Декабрь', ]
if month in month_d:
    print(month_d[month])
    print(month_l[month])
else:
    print('Ошибка, введите числа в диапозоне от 1 до 12')
