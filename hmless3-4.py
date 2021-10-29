def myfun(x, y):
    try:
        end = x ** y
    except TypeError:
        return 'Введите первое положительное и второе отрицательное число'
    return end


print(myfun(5.3, -5))
