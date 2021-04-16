text_file = open("calc.txt")

def calc (operand_1, operation, operand_2):
    # TODO Решено правильно, но, давайте объединим условные операторы if в один с помощью блоков elif/else.
    #  Каждый условный оператор if это новая проверка, которая производится всегда.
    #  В то время, как блоки elif и else могут и не наступить.
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
    # TODO, функция должна возвращать результат вычислений.
    #  т.к. в итоге, нам необходимо получить сумму всех результатов.

# TODO, лишняя функция. При помощи какого строкового метода можно узнать, является ли строка числом?
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
    if is_number(operand_1) == False or is_number(operand_2) == False:  # TODO вместо "== False", лучше использовать "not"
        raise BaseException ("Использовать можно только цифры")
        # TODO BaseException - внутренняя ошибка python. Уровнем выше есть Exception.
        #  Предлагаю вызывать именно Exception, PyCharm не будет ругаться =)

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
