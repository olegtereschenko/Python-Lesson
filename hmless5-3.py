# stufman = open('hmless5-3.txt', 'r', encoding='utf-8')
# new_list = stufman.readlines()
# print(new_list)
# stufman.close()
# with open("hmless5-3.txt", "r", encoding='utf-8') as file:
#     for st in open ( "hmless5-3.txt" ):
#         line = st.split()[1]
#         print(line)
# while True:
#     if int(line) <= 20000:
#         break
with open('hmless5-3.txt', 'r', encoding='utf-8') as file:
    setlist = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f'Примерно поровну = {round(sum(setlist.values()) / len(setlist), 3)}\n'
          f'Кто получает меньше 20К {[i[0] for i in setlist.items() if i[1] <= 20000]}')
