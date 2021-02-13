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
            if sym == "0":
                num2 += 10 ** chek2 - 1
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
    word2.insert(ind1, str(number1))
# от скобок избавились -)
if "*" in word2: # Определение индексов
    indc = word2.index("*")
else:
    indc = str(len(word2) + 1)

if "-" in word2:
    indmin = word2.index("-")
else:
    indmin = str(len(word2) + 1)

if "+" in word2:
    indplus = word2.index("+")
else:
    indplus = str(len(word2) + 1)

word3 =[]
word5 = word2 [:]
if int(indc) < int(indmin) and int(indmin) < len(word2) + 1 and int(indmin) < int(indplus):
    word3 = word2 [0: indmin]
    for sym in word3:
        word2.pop(0)
    word4 = evl(word3)
    word2.insert(0, str(word4))
elif int(indc) < int(indmin) and int(indplus) < int(indmin):
    word3 = word2 [0 :indplus]
    for sym in word3:
        word2.pop(0)
    word4 = evl(word3)
    word2.insert(0, str(word4))

if int(indc) > int(indmin) and int(indmin) < len(word2) +1 and int(indmin) < int(indplus):
    word3 = word2 [int(indmin) + 1 : int(indplus) - 1]
    for sym in word3:
        word2.pop(indmin)
    word4 = evl(word3)
    word2.insert(indmin, str(word4))
elif int(indc) < int(indplus) and int(indplus) < int(indmin):
    word3 = word2 [int(indplus) +1: int(indmin) - 1]
    for sym in word3:
        word2.pop(indmin)
    word4 = evl(word3)
    word2.insert(indplus, str(word4))
print(word3)
print(word2)
word = evl(word2)

print(f"ответ {word}")
# проше было бы использовать eval
# , предлагаю реализовать несколько функций. Для умножения, сложения и вычитания.
#  + Возможно функцию для раскрытия скобок. Функция должна будет брать код в скобках
#  и применять к нему одну из наших функций. И возвращать итог, для дальнейшей работы алгоритма =)

# TODO Выражение: (5+4)*2-10+5
#  ['9', '*', '2']
#  ['18', '-', '1', '0', '+', '5']
#  ответ 528
#  Правильный ответ 13 =)