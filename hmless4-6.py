from itertools import count, cycle

count_1 = count(-5)
cycle_1 = cycle('ng656ft5e5dyu7t6f')

for a in range(10):
    print('(count_1,cycle_1) = ({},{})'.format(next(count_1), next(cycle_1)))
