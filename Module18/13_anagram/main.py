first_word = input("Введите первое слово: ")
second_word = input("Введите второе слово: ")
chek = True

for symbol in first_word:
    if not second_word.count(symbol):
        print("Слова не являются анаграммами друг друга")
        chek = False
        break
    else:



if chek == True:
    print("Слова являются анаграммами друг друга")