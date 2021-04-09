import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print("в f: на ноль делить нельзя")


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError:
        print("в f2: на ноль делить нельзя")


try:
    file = open('coordinates.txt', 'r')
    for line in file:
        num_x, num_y = line.split()
        res1 = f(int(num_x), int(num_y))
        res2 = f2(int(num_x), int(num_y))
        number = random.randint(0, 100)
        file_2 = open('result.txt', 'a')
        if file_2.closed:
            raise ("result.txt закрыт")
        my_list = sorted([res1, res2, number])
        file_2.write("{} \n".format(' '.join(str(my_list))))
except FileNotFoundError:
    print("Что-то пошло не так")
finally:
    file.close()
    file_2.close()


# TODO отредактировать и исправить программу
