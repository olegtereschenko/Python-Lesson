def info(name, surname, year, city, mail, tel):
    print(
        f"Ваша имя и фамилия {name + surname}, вы родились в {year} году в городе {city}, ваша почта {mail} и телефон {tel}")


info(name=input('Ваше имя '), surname=input('Ваша фамилия '), year=input('Год рождения '),
     city=input('Город рождения '), mail=input('Ваша почта '), tel=input('Телефон '))


# Второй варинат (с именноваными аргументами)
def info(name, surname, year, city, mail, tel):
    return f"name - {name}, surname - {surname}, year - {year}, city - {city}, mail - {mail}, tel - {tel}"


print(info(name="bany", surname="bizi", year="2234", city="SPB", mail="pochta@gde.net", tel="0998765421"))
