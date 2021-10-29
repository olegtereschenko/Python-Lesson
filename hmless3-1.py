def result(first, second):
    try:
        first, second = int(first), int(second)
        result = first / second
    except ValueError:
        return "Введите числа, а не что то другое"
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return result()


print(result(input("Введите число которое нужно поделить: "), input("Введите число на которое надо делить: ")))
