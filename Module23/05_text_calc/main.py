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

def chek_data (i_line):
    if i_line.split != 3:
        raise ValueError ("Что-то не так с уровнением")
    if operation not in all_operation:
        raise ValueError ("operation не является символами +, -, *, /, %")
    if is_number(operand_1) == False or is_number(operand_2) == False:
        raise BaseException ("Использовать можно только цифры")


for i_line in text_file:
    try:
        operand_1, operation, operand_2 = i_line.split()
    except ValueError:
        print("Что то не так с уровнением")
    all_operation = "+-/%*"
    try:
        if operation not in all_operation:
            raise ValueError
        if is_number(operand_1) == False or is_number(operand_2) == False:
            raise BaseException
    except ValueError:
        print("operation не является символами +, -, *, /, %")
    except BaseException:
        print("Использовать можно только цифры")
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

#Z Я не понял как ловить ошибки в основной программе из функций
# TODO, Предлагаю оптимизировать код в текущей программе, нам потребуется 2 функции.
#  1. для проверки корректности данных и вызова исключения, если данные не корректные.
#  2. для произведения действий, если данные корректные.
#  Ловить ошибки необходимо только в основном цикле программы, одним блоком try/except.
