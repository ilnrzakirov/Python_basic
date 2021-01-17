word = input("Введите слово: ")
word_list = []
remains = 0
flag = True

for symbol in word:
    word_list.append(symbol)


# TODO, а как решить без индексов и срезов? Ведь если решить через них, то циклы не нужны =)
for symbol in word[::-1]:
    if symbol != word[remains]:
        flag = False
        break
    remains += 1

if flag == True:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
