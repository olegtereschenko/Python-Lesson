from sys import argv


def money():
    try:
        hours, rate, bonus, kvartal = map(float, argv[1:])  # kvartal- квартальная премия раз в 3 месяца :) хочется всегда больше
        print(f'MONEY - {hours * rate + bonus + (kvartal * 0.33)}')
    except ValueError:
        print('Введите 4 числа')


money()
