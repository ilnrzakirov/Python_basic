import os


def code_counter(path):
    result = 0
    directory = path  # директория для подсчета
    for path in os.listdir(directory):
        new_path = directory + "".join(path)
        if str(new_path).endswith(".py"):
            with open(str(path), "r") as file:
                 # , глобальная переменная получилась лишней.
                for line in file:
                    # , возможно, стоит просто идти по строке, проверяя, что первый символ не "#"
                    #  split возможно лишний.
                    if line:
                        if not line.startswith("#"):
                            result += 1
    return result


# TODO, директорию необходимо запросить у пользователя и передать в функцию.
#  Максимальный уровень вложенности кода не должен превышать 3. Возможно, стоит разбить нашу функцию на несколько функций. =)

# path = input("Введите директорию для подсчета: ")

print(code_counter(path=os.getcwd()))
