class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
print("Вводите целые числа, чтобы формировать список, но если хотите остановить оставьте строчку пустой и нажмите Enter")
while True:
    inp_data = input(f"Введите число: ")
    if inp_data == "":
        break
    try:
        if inp_data.replace("-", "").replace("-", "").isdigit():
            my_list.append(float(inp_data))
        else:
            raise OwnError("Не похоже на число")
    except OwnError as err:
        print(err)
        continue

print(my_list)