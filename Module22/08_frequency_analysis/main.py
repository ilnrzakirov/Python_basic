input_text = open("text.txt", "r")
alfabit = "abcdefghijklmnopqrstuvwxyz"
sym_dict = dict()

# Составление словаря с количестовом букв в тексте
for i_line in input_text:
    for sym in i_line.lower():
        if sym in alfabit:
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1

all_sym = 0
# Нахождение общего количества букв
for value in sym_dict.values():
    all_sym += value
# Составление словаря ключ - очки, значение - буквы
share_dict = dict()
for name, value in sym_dict.items():
    share = value / all_sym
    round_share = round(share, 3)
    sym_dict[name] = round_share
    if round_share in share_dict:
        share_dict[round_share].append(name)
    else:
        # TODO, последующие 2 действия предлагаю объединить в одно. Мы же можем создавать значение
        #  как список из 1 элемента =)
        share_dict[round_share] = []
        share_dict[round_share].append(name)

# Сортировка значений словаря share_dict
for key, value in share_dict.items():
    share_dict[key] = sorted(value)

print(share_dict)
print(sym_dict)
analysis_file = open("analysis.txt", "a")

# Запись результатов в файл
for key, value in share_dict.items():
    for item in value:
        # TODO, запись в файл возможно стоит сделать без дополнительной переменной
        #  При помощи форматирования строк =)
        write_string = item + " " + str(key) + "\n"
        analysis_file.write(write_string)

input_text.close()
analysis_file.close()