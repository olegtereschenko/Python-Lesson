guest = input('Введите любые данные: ')
with open("hmless5-1.txt", "w", encoding='utf-8') as file:
    file.writelines("%s\n" % line for line in guest)
