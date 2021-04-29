import random


def one_day():
    number = random.randint(1, 10)
    # TODO, эта функция ловить ошибки не должна.
    #  только вызывать. Ловить необходимо внутри основного цикла программы.
    try:
        if number == 8:
            error = random.choice(err)
            with open("karma.log", "a") as karma_log:
                karma_log.write(error + "\n")
            raise error
    except:  # TODO, давайте вспомним как правильно ловить ошибки =)
        print("Ошибка: {}".format(error))

    return random.randint(1, 7)


# TODO, таким образом храним в списке текст. А как хранить классы? =)
err = ["KillError", "DrunkError", "CarCrashError", "GluttonyError", "DepressionError"]
karma = 0

while karma < 500:
    karma += one_day()
    print("Карма: {}".format(karma))
