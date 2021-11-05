from random import randint

with open('hmless5-5.txt', 'w', encoding='utf-8') as new_file:
    list = [randint(1, 500) for i in range(500)]
    new_file.write(' '.join(map(str, list)))
print(f'Сумма всех чисел: {sum(list)}')
