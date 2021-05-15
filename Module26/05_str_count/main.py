import os


def code_counter():
    result = 0
    directory = os.getcwd()  # директория для подсчета
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



print(code_counter())
