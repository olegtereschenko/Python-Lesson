russ = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('hmless5-4-1.txt', 'w', encoding='utf-8') as file:
    with open('hmless5-4.txt', encoding='utf-8') as file_1:
        file.writelines([line.replace(line.split()[0], russ.get(line.split()[0])) for line in file_1])
