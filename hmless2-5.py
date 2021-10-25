rating = [9, 8, 8, 7, 5, 4, 4, 4, 3, 2, 1, 1, 0]
new_rating = int(input('Введите новый элемент рейтинга в виде натурального числа - '))
i = 0
for n in rating:
    if new_rating <= n:
        i += 1
    else:
        break
rating.insert(i, new_rating)
print(rating)
