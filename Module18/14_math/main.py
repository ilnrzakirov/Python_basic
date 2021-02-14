word = input("Выражение: ")


def multy(list):
    num1 = ""
    num2 = ""
    ind = list.index("*")
    num1list = list[:ind]
    num2list = list[ind + 1:]
    for sym in num1list:
        num1 += str(sym)
    for sym in num2list:
        num2 += str(sym)
    result = int(num1) * int(num2)
    return result


def minus(list):
    num1 = ""
    num2 = ""
    ind = list.index("-")
    num1list = list[:ind]
    num2list = list[ind + 1:]
    for sym in num1list:
        num1 += str(sym)
    for sym in num2list:
        num2 += str(sym)
    result = int(num1) - int(num2)
    return result


def plus(list):
    num1 = ""
    num2 = ""
    ind = list.index("+")
    num1list = list[:ind]
    num2list = list[ind + 1:]
    for sym in num1list:
        num1 += str(sym)
    for sym in num2list:
        num2 += str(sym)
    result = int(num1) + int(num2)
    return result


word2 = list(word)
if word.count(")"):  # Решение внутри скобок
    ind1 = word.index("(")
    ind2 = word.index(")")
    word1 = word[ind1 + 1: ind2]
    if "+" in word1:
        number1 = plus(word1)
    elif "-" in word1:
        number1 = minus(word1)
    for num in range(len(word1) + 2):
        word2.pop(ind1)
    word2.insert(ind1, str(number1))

word1 = []
if "*" in word2:
    chek = 0
    for sym in word2:
        if chek == 0:
            if sym == "+" or sym == "-":
                word1 = []
                continue
        if sym == "*":
            chek = 1
        if chek == 1:
            if sym == "+" or sym == "-":
                ind = word2.index(sym)
                word2.insert(ind, '&')
                break
        word1.append(sym)
    number1 = multy(word1)
    ind2 = word2.index("&")
    word2[ind2 - len(word1): ind2 + 1] = str(number1)
word1 = []
if "*" not in word2:
    chek = 0
    for sym in word2:
        if chek == 1:
            if sym == "+" or sym == "-":
                break
        if chek == 0:
            if sym == "+" or sym == "-":
                chek = 1
        word1.append(sym)
    if "+" in word1:
        number1 = plus(word1)
        for _ in range(len(word1)):
            word2.pop(0)
        word2.insert(0, str(number1))
    elif "-" in word1:
        number1 = minus(word1)
        for _ in range(len(word1)):
            word2.pop(0)
        word2.insert(0, str(number1))
else:
    pass
word1 = []
if "+" or "-" in word2:
    chek = 0
    for sym in word2:
        if chek == 1:
            if sym == "+" or sym == "-":
                break
        if chek == 0:
            if sym == "+" or sym == "-":
                chek = 1
        word1.append(sym)
    if "+" in word1:
        number1 = plus(word1)
        for _ in range(len(word1)):
            word2.pop(0)
        word2.insert(0, str(number1))
    elif "-" in word1:
        number1 = minus(word1)
        for _ in range(len(word1)):
            word2.pop(0)
        word2.insert(0, str(number1))

print(word2)

# проше было бы использовать eval
# , предлагаю реализовать несколько функций. Для умножения, сложения и вычитания.
#  + Возможно функцию для раскрытия скобок. Функция должна будет брать код в скобках
#  и применять к нему одну из наших функций. И возвращать итог, для дальнейшей работы алгоритма =)

#  Выражение: (5+4)*2-10+5
#  ['9', '*', '2']
#  ['18', '-', '1', '0', '+', '5']
#  ответ 528
#  Правильный ответ 13 =)
# зачёт!
