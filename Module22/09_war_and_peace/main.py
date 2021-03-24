import zipfile

import operator
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
# TODO, для сортировки словаря, предлагаю создать список из ключею и значений
#  и применить к нему списковый метод sort(). Получится всего 2 строки кода =)
        # TODO, последующие 2 действия предлагаю объединить в одно. Мы же можем создавать значение
        #  как список из 1 элемента =)


sym_list = list(sym_dict.items())
sym_list.sort(key=operator.itemgetter(1, 0))

analysis_file = open("analysis.txt", "a", encoding="UTF-8")

# Запись результатов в файл
for item in sym_list:
        # TODO, запись в файл возможно стоит сделать без дополнительной переменной
        #  При помощи форматирования строк =)
    analysis_file.write(f"{item[0]} {str(item[1])} \n")

analysis_file.close()
text_document.close()
voyna_i_mir.close()
