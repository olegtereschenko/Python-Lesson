from random import randint

list1 = [randint(-50, 50) for _ in range(20)]
list2 = [el for el in list1 if list1.count(el) == 1]
print(f'Исходный лист:{list1}\nСформированный список:{list2}')
