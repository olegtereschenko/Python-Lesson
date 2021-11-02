from functools import reduce


def my_fanc(el_1, el_2):
    return el_1 + el_2


new_list = [el for el in range(100, 1001, 2)]
print(f'Список:{new_list}\nПроизведение:{reduce(my_fanc, new_list)}')
