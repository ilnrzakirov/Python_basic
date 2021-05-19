import os


#  директория 'C:\\...\\ilnur_zakirov\\python_basic\\Module26\\05_str_count'
#  Пока что превратилась в 'C:\\...\\ilnur_zakirov\\python_basic\\Module26\\05_str_countmain.py'
#  Предлагаю объединять директории при помощи метода join модуля os.
#  К сожалению, строковый метод join в данном задании не лишний
def code_counter(path):
    result = 0
    directory = path  # директория для подсчета
    for ipath in os.listdir(directory):
        new_path = os.path.join(directory, ipath)
        if str(new_path).endswith(".py"):
            result += code_counter_next(new_path)
            # , в этом месте стоит сразу передавать ipath
            #  иначе, если файл находится не в текущей директории, то наша функция его не видит.
    return result


def code_counter_next(path):
    result = 0
    # , str возможно лишнее =)
    with open(path, "r") as file:
        # , глобальная переменная получилась лишней.
        for line in file:
            # , возможно, стоит просто идти по строке, проверяя, что первый символ не "#"
            #  split возможно лишний.
            # , в условном операторе ниже стоит попробовать убрать лишний символ "\n" из строки при помощи строкового метода.
            #  иначе, строка с одним символом "\n" считается не пустой.
            if line:
                if not line.strip().startswith("#") and line != "\n":
                    result += 1
    return result


# , директорию необходимо запросить у пользователя и передать в функцию.
#  Максимальный уровень вложенности кода не должен превышать 3. Возможно, стоит разбить нашу функцию на несколько функций. =)

path = input("Введите директорию для подсчета: ")

print(code_counter(path=path))

# зачёт!
