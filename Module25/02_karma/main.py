import random


class Error:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def one_day():
    number = random.randint(1, 10)
    # , эта функция ловить ошибки не должна.
    #  только вызывать. Ловить необходимо внутри основного цикла программы.

    if number == 8:
        # , в этой функции запись в файл не нужна.
        #  Стоит записывать в файл в основном цикле программы
        raise random.choice(err)
        # , предлагаю в этом месте вызывать исключение из списка err.
        #  При помощи какого метода модуля random можно получить случайный элемент списка? =)
    # , давайте вспомним как правильно ловить ошибки =)
    return random.randint(1, 7)


# , таким образом храним в списке текст. А как хранить классы? =)
KillError = Error("KillError")
DrunkError = Error("DrunkError")
CarCrashError = Error("CarCrashError")
GluttonyError = Error("GluttonyError")
DepressionError = Error("DepressionError")
err = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
karma = 0

while karma < 500:
    try:
        karma += one_day()
        print("Карма: {}".format(karma))
    except Exception:
        error = random.choice(err)
        with open("karma.log", "a", encoding="UTF-8") as karma_log:
            karma_log.write("Ошибка: {} \n".format(error))  # TODO, записывать в файл предлагаю при помощи форматирования =)
        print("Ошибка: {}".format(error))
