zen = open("zen.txt", "r")
alfabit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym_dict = dict()
line_count = 0
sym_count = 0
word_count = 0
for i_line in zen:
    line_count += 1
    for i_elem in i_line:
        if i_elem in alfabit:
            sym_count += 1
            # , для сокращения количества вычислений в коде, предлагаю создать переменную, равную i_elem.lower()
            #  И далее, в коде, работать с ней.
            element_line = i_elem.lower()
            if element_line in sym_dict:
                sym_dict[element_line] += 1
            else:
                sym_dict[element_line] = 1
        if i_elem == " ":
            word_count += 1

sorted_dict = sorted(sym_dict, key=sym_dict.get)

print("Количество строк: ", line_count)
print("Количество букв: ", sym_count)
print("Количество слов: ", word_count)
print("Буква {} встречается меньше остальных, в {} местах".format(sorted_dict[0], sym_dict[sorted_dict[0]]))

zen.close()

# зачёт!
