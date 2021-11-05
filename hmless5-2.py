my_list = open('hmless5-2.txt', 'r', encoding='utf-8')
print(f'Всего строк в файле:')
print((len(my_list.readlines())))
my_list.seek(0)
i = 0
for line in my_list:
    i
    i += 1
    print(f'Сколько символом в строке {i}')
    print(int(len(line)) - 1)
my_list.close()
