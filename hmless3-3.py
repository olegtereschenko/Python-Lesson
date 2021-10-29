my_func = lambda n_1, n_2, n_3: (n_1 + n_2 + n_3) - min(n_1, n_2, n_3)
print(my_func(n_1=int(input('1 цифра: ')), n_2=int(input('2 цифра: ')), n_3=int(input('3 цифра: '))))
# либо так без - запроса ввода
print(my_func(44, 56, 23))
