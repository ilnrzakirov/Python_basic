first_word = input("Введите первое слово: ")
second_word = input("Введите второе слово: ")
chek = True

for symbol in first_word:
    if first_word.count(symbol) != second_word.count(symbol):
        print("Слова не являются анаграммами друг друга")
        chek = False
        break
if chek:
    print("Слова являются анаграммами друг друга")

# зачёт!
