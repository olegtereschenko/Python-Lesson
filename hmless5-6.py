with open('hmless5-6.txt', 'r', encoding='utf-8') as file:
    file_1 = file.readlines()
    for file_2 in file_1:
        file_3 = ''.join((i if i in '1234567890' else ' ') for i in file_2)
        file_new = [int(float(i)) for i in (file_3.split())]
        print(f'{file_2.split()[0]} {sum(file_new)}')
