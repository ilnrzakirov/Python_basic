text_file = open("calc.txt")

def calc (operand_1, operation, operand_2):
    if operation == "+":
        result = float(operand_1) + float(operand_2)
    if operation == "-":
        result = float(operand_1) - float(operand_2)
    if operation == "*":
        result = float(operand_1) * float(operand_2)
    if operation == "/":
        result = float(operand_1) / float(operand_2)
    if operation == "%":
        result = float(operand_1) % float(operand_2)
    print("Результат: {}".format(result))

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def chek_data (i_line, count):
    if len(i_line.split()) != 3:
        raise ValueError ("Что-то не так с уровнением")
    operand_1, operation, operand_2 = i_line.split()
    if operation not in all_operation:
        raise ValueError ("operation не является символами +, -, *, /, %")
    if is_number(operand_1) == False or is_number(operand_2) == False:
        raise BaseException ("Использовать можно только цифры")
    if len(operation) > 1:
        print("Обнаружена ошибка в строке {} {} желаете исправить?: ".format(count, i_line))
        answer = input().lower()
        if answer == "да":
            corrected = input("Введите исправленную версию: ")
            try:
                operand_1, operation, operand_2 = corrected.split()
            except ValueError:
                print("Что то не так с уровнением")
        if answer == "нет":
            raise ValueError ("Некорректные данные")

all_operation = "+-/%*"
count = 0
for i_line in text_file:
    count +=1
    try:
        chek_data(i_line)
        operand_1, operation, operand_2 = i_line.split()
        calc(operand_1, operation, operand_2)
    except (ValueError, BaseException):
        print("Что то не то с уровнением")

