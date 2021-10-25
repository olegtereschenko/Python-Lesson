# newlist = input('Введите любые символы через запятую:' )
# secondlist = newlist.split()
# length = len(secondlist)
# i = 0
# for i in range(length):
#    print(str(i+1), type(secondlist[i]))
# пытался сделать с вводом пользователя но безуспешно :((( будет так
list1 = [1, 5, 3.6, 'f', 'back', False]
i = 0
while i < len(list1):
    print(type(list1[i]))
    i += 1
