word = input("Выражение: ")
symbol = "+-*"
plus = "+"
minus = "-"
mlt = "*"


def evl (list): # Функция для умножения\сложения\вычитания двух чисел
    chek = 0
    chek1 = 0
    chek2 = 0
    num1 = 0
    num2 = 0
    result = 0
    for sym in list:
        if sym in symbol:
            chek = 1
            continue
        if chek == 0:
            num1 += int(sym) * (10 ** chek1)
            chek1 += 1
        if chek == 1:
            num2 += int(sym) * (10 ** chek2)
            chek2 += 1
    for sym in list:
        if sym in plus:
            result = num1 + (num2)
        elif sym in minus:
            result = num1 - (num2)
        elif sym in mlt:
            result = num1 * (num2)
    return result


list(word)
word2 = list(word)
if word.count(")"): # Решение внутри скобок
    ind1 = word.index("(")
    ind2 = word.index(")")
    word1 = word[ind1 + 1: ind2]
    number1 = evl(word1)

# Решать внутри скобок научились, дальше не понятно. думаю для начала надо подставить значение в общее уровнение
    for num in range (len(word1) + 2):
        word2.pop(ind1)
    word2.insert(0, number1)
# от скобок избавились -)



print(number1)
print(f"ответ {word}")

# TODO, предлагаю реализовать несколько функций. Для умножения, сложения и вычитания.
#  + Возможно функцию для раскрытия скобок. Функция должна будет брать код в скобках
#  и применять к нему одну из наших функций. И возвращать итог, для дальнейшей работы алгоритма =)
