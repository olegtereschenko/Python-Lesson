import json

with open('hmless5-7.json', 'w', encoding='utf-8') as file_1:
    with open('hmless5-7.txt', encoding='utf-8') as file_2:
        file_3 = {f.split()[0]: int(f.split()[2]) - int(f.split()[3]) for f in file_2}
        file_end = [file_3, {"Прибыль": round(sum([int(i) for i in file_3.values() if int(i) > 0]) /
                                              len([int(i) for i in file_3.values() if int(i) > 0]))}]
    json.dump(file_end, file_1, ensure_ascii=False, indent=4)
