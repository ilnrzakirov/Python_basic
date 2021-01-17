word = input("Введите слово: ")
word_list = []
remains = 0
flag = True

for symbol in word:
    word_list.append(symbol)
# TODO, а как решить без индексов и срезов? Ведь если решить через них, то циклы не нужны =)
# TODO, как в цикле записать слово наоборот? Помните задание с сэндвичем? =)



if flag == True:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
