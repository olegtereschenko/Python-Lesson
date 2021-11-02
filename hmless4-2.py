# mylist1 = [23,534,2,34,56,98,45]
# mylist2 = [mylist1[num] for num in range(1,len(mylist1)) if mylist1[num]>mylist1[num - 1]]
# print(mylist2)
# 1 способ - без генератора

from random import randint

costumlist = [randint(-5000, 10000) for n in range(0, randint(5, 40))]
secondlist = [num for i, num in enumerate(costumlist[1:]) if num > costumlist[i]]
print(costumlist)
print(secondlist)
