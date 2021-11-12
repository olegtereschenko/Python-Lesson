# # # # Перезагрузка операторов (magic method)
# # # # __init__() - соотв конструктору объектов класса, срабатывает при создании объекта
# # # # __del__() соотв деструктору обектов класса, срабатывает при удалении объектов
# # # # __str__() срабатывает при передаче объекта функции str() и print(), преобразует объект к строке
# # # # __add__() срабатывает при участии объекта в операции сложения в качестве операнда с левой стороны,
# # # #             обеспечивая перезагрузку оператора сложения
# # # # __selattr__() срабатывает при выполненни операции присваивания хначения атрибуту объекта
# # # # __getitem__() срабатывает при извлечении элемента по индексу
# # # # __cal__() срабатывает при обращении к экземпляру класса как к функции
# # # #
# # # # __gt__() соответсвует оператору >
# # # # __lt__() <
# # # # __ge__() >=
# # # # __le__() <=
# # # # __eq__() ==
# # # # __iadd__() += сложение и присваивание
# # # # __isub__() -= вычитание и присваивание
# # # #ример 1
# # # class MyClass:
# # #     def __init__(self,f_1):
# # #         self.f_1 = f_1
# # #     def __del__(self):
# # #         # print("объект удален") #мусорщик чтобы удалять и разгружать систему
# # # # first = MyClass(90)
# # # # del first #можно удалить объект
# # # # print(first.f_1)
# #
# # #пример 2
# #
# # # class MyClass:
# # #     def __init__(self,f_1,f_2):
# # #         self.f_1 = f_1
# # #         self.f_2 = f_2
# # #
# # #     def __str__(self):
# # #         return f'f_1:{self.f_1},f_2:{self.f_2}.'
# # #
# # # first = MyClass(90,70)
# # # print(first)
# #
# # # пример 3 сумма
# # class MyClass:
# #     def __init__(self, f_1, f_2):
# #         self.f_1 = f_1
# #         self.f_2 = f_2
# #
# #     def __str__(self):
# #         return f'f_1:{self.f_1},f_2:{self.f_2}.'
# #
# #     def __add__(self, other):
# #         return MyClass(self.f_1 +other.f_1, self.f_2 + other.f_2)  #получится кортеж двух функций
# #
# # first = MyClass(90, 70)
# # second = MyClass(89,321)
# # print(first + second)
#
# # пример 4
#
# class MyClass:
#     def __init__(self, f_1):
#         self.f_1 = f_1
#
#
#     def __str__(self):
#         return f'f_1:{self.f_1}'
#
#     def __call__(self, new_f_1):
#         self.f_1 = new_f_1
#
# first = MyClass(90)
# second = MyClass(89)
# print(first,second)
#
# first('apple') #замена
# print(first,second)
#
# Переопределение методов - спецальный механизм позволящий использовать метод класса родителя в классе потомке с
# добавлением некторой функциональности
#
# Интерфейсы
# Под интрефейсом в ООП понимается описание поведения объекта, те своокупность публичных методов объекта которые могут
# применяться в других частях программы для взаимодействия с ним
# пример 5
# from abc import ABC, abstractmethod  # Декоратор
#
#
# class Cats(ABC):
#     @abstractmethod
#     def roar(self):
#         pass
#
#     @abstractmethod
#     def purr(self):
#         pass
#
#
# class Tiger(Cats):
#     def roar(self):
#         print('HHHHRRR')
#
#     def purr(self):
#         print('mur')
#
#     def m_1(self):
#         print('HI')
#
#
# tiger_1 = Tiger
# Интерфейс итерации
# Под итераторами понимаются спец объекты, обеспечивающие пошаговый доступ к данным из котейнера.
# В привязке к итераторам работают циклы перебора (for in), встроенные функции (map(), filter(),zip()) операция распаковки
# Работа и итераторами
# Итератор в Python - объект, реализующий метод __next__ без аргументов, возвращающий очередной элемент или исключение StopIteration
# 1)вызов метода __iter__() для итеруремого объкта. Метож __iter__ возвращает объект с методом __next__
# 2)цикл for in в ходе каждой итерации запускает метод __next__ который при каждом вызове возвращает очередной элемент итератора
# 3)когда элементы итератора исчерпаны, метод __next__ завершает работу и генерирует исключение Stopiteration

#Primer 6
#
# class Iterator:
#     """
#     объект-итератора
#     """
#     def __init__(self,start=0):
#         self.i=start
#         #у итератора есть метод __next__
#
#     def __next__(self):
#         self.i += 1 #шаг
#         if self.i <= 5: #максимум
#             return self.i
#         else:
#             raise StopIteration
# class IterObj:
#     """
#     объект, поддерживащий интерфейс итерации (итеруруемый объект)
#     """
#     def __init__(self, start = 0):
#         self.start = start - 1 #потому что возвращаем объект и надо отнять единицу или начало перебора выпадет
#
#     def __iter__(self):
#         #метод iter должен возвращать объект-итератор
#         return Iterator(self.start)
#
# obj = IterObj(start=2)
# for el in obj:
#     print(el)
#
# # Декоратор @property
# # Под декоратором в Python подразумевается функция (или класс), расширяющая логику работы другой
# # функции. Встроенный декоратор @property позволяет работать с методом некоторого класса как с атрибутом
#
# class MyClass:
#     def __init__(self,param_1,param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#
#     @property
#     def my_method(self):
#         return f'параметры переданные в класс:'\
#                f'{self.param_1},{self.param_2}'
#
# mc = MyClass('text_1',"text_2")
# # print(mc.my_method)
#
# #primer!
# class Auto:
#     def __init__(self,year):
#         self.year = year
#
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def year(self,year):
#         if year <2000:
#             self.__year = 2000
#         elif year >2021:
#             self.__year = 2021
#         else:
#             self.__year = year
#     def get_auto_year(self):
#         return f'Автомобиль выпущен в {str(self.year)} годуЭ'
#
# auto_1 = Auto(2005)
# print(auto_1.year)

#Композиция
#В концепции ООП существует возможность реализации композиционного подхода, в соответсвии с которым создается
# класс-контейнер включабщий вызовы других классов

class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height

class Room:
    def __init__(self,len_1,len_2,height):
        self.square = 2*height*(len_1+len_2)
        self.wd = []

    def add_win_door(self,wd_len,wd_height):
        self.wd.append(WindowDoor(wd_len,wd_height))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square

r = Room(7,4,3.7)
print(r.square)

r.add_win_door(2,4)
r.add_win_door(2,1)
r.add_win_door(2,3)
print(r.common_square())
