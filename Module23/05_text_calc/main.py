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
    if len(i_line.split()) != 3:
        raise ValueError ("Что-то не так с уровнением")
    operand_1, operation, operand_2 = i_line.split()
    if operation not in all_operation:
        raise ValueError ("operation не является символами +, -, *, /, %")
    if is_number(operand_1) == False or is_number(operand_2) == False:
        raise BaseException ("Использовать можно только цифры")

all_operation = "+-/%*"
for i_line in text_file:
    try:
        chek_data(i_line)
        operand_1, operation, operand_2 = i_line.split()
        calc(operand_1, operation, operand_2)
    except (ValueError, BaseException):
        print("Что то не то с уровнением")



#Z Я не понял как ловить ошибки в основной программе из функций
# TODO, Предлагаю оптимизировать код в текущей программе, нам потребуется 2 функции.
#  1. для проверки корректности данных и вызова исключения, если данные не корректные.
#  2. для произведения действий, если данные корректные.
#  Ловить ошибки необходимо только в основном цикле программы, одним блоком try/except.
