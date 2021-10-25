listguest = input('Введите числа разделенные пробелами: ').split()
for a, i in enumerate(listguest, 1):
    print(a, i) if len(i) < 11 else print(a, i[:10])
