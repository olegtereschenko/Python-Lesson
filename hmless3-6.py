def func():
    for text in input('Введите текст через пробел латиницей (без заглавных букв):\n').split():
        elements = 0
        for element in text:
            if 97 <= ord(element) <= 122:
                elements += 1
        print(text.title() if elements == len(text) else f'{text} - только маленькие латинские буквы')


func()
