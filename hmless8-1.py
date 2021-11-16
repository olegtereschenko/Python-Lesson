
class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def change_type(cls, date):
        return f'День {int(date[0]):02d}, Месяц {int(date[1]):02d}, Год {int(date[2])}'

    @staticmethod
    def validation(date):
        if not int(date[0]) in range(1, 32) or not int(date[1]) in range(1, 13) or int(date[2]) > 3000:
            return 'Введена некорректная дата!'

    def date_func(self):
        result_1 = Data.change_type(self.date.split('-'))
        result_2 = Data.validation(self.date.split('-'))
        return result_2 if result_2 else f'\n{result_1}'


user_date = input('Введите дату: (чч-мм-гг): ')
date_1 = Data(user_date)
print(date_1.date_func())
user_date = input('Введите дату: (чч-мм-гг): ')
date_2 = Data(user_date)
print(date_2.date_func())
print(date_1.date_func())