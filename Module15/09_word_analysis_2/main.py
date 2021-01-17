word = input("Введите слово: ")
word_list = []
remains = 0

# Цикл лишний, можно сразу в цикле идти по word
for symbol in word:
    word_list.append(symbol)
# , а как решить без индексов и срезов? Ведь если решить через них, то циклы не нужны =)
# , как в цикле записать слово наоборот? Помните задание с сэндвичем? =)

revers = ""
for symbol in word_list:
    revers = symbol + revers
print(revers)

if word == revers:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

# зачёт!
