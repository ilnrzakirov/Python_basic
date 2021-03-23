import zipfile
# Распаковка и открытие файла
voyna_i_mir = zipfile.ZipFile("voyna-i-mir.zip", "r")
voyna_i_mir.printdir()
text_document = open(voyna_i_mir.extract("voyna-i-mir.txt"), "r", encoding="UTF-8")

alfabit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
sym_dict = dict()

# Составление словаря букв с использованным количеством в файле
for i_line in text_document:
    for sym in i_line:
        if sym in alfabit:
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1

# Составление перевернутого словаря
share_dict = dict()
for name, value in sym_dict.items():
    share = value
    if share in share_dict:
        share_dict[share].append(name)
    else:
        share_dict[share] = []
        share_dict[share].append(name)

# Сортировка словаря
key_sorted = sorted(share_dict)
sorted_share_dict = dict()
for key in key_sorted:
    sorted_share_dict[key] = share_dict[key]

for key, value in sorted_share_dict.items():
    sorted_share_dict[key] = sorted(value)

analysis_file = open("analysis.txt", "a", encoding="UTF-8")

# Запись результатов в файл
for key, value in sorted_share_dict.items():
    for item in value:
        write_string = item + " " + str(key) + "\n"
        analysis_file.write(write_string)

analysis_file.close()
text_document.close()
voyna_i_mir.close()
