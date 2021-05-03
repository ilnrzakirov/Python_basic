import random

class Error:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def one_day():
    number = random.randint(1, 10)
    # TODO, эта функция ловить ошибки не должна.
    #  только вызывать. Ловить необходимо внутри основного цикла программы.

    if number == 8:
        error = random.choice(err)
        with open("karma.log", "a") as karma_log:
            karma_log.write(str(error) + "\n")
        raise error.name
      # TODO, давайте вспомним как правильно ловить ошибки =)
    return random.randint(1, 7)


# TODO, таким образом храним в списке текст. А как хранить классы? =)
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
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError ) as err:
        print("Ошибка: {}".format(err))
