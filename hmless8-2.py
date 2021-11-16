class Number (Exception):
    def __init__(self, txt):
        self.txt = txt


def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        if s_2 == 0:
            raise Number('Делить на ноль нельзя!ТОЧНО!')
        return round(s_1 / s_2, 3)
    except ValueError:
        return "Ошибочка"
    except Number as num:
        return num


print(div(input("Числитель - "), input("Знаменатель - ")))