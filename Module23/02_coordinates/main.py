import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    # , в наших функциях не нужно вызывать исключения.
    #  Выпадут сами, если делитель будет равен "0"
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


file_2 = open('result.txt', 'a')
file = open('coordinates.txt', 'r')
for line in file:
    try:
        # , стоит ловить ошибки в цикле, иначе, программа завершает свою работу наткнувшись на ошибку в цикле.
        num_x, num_y = line.split()
        # TODO, проверки ниже получились лишние.
        #  В данном задании нем не нужно вызывать ошибки, только ловить их.
        #  Предлагаю сначала ловить ошибку функции f, после этого ловить ошибку в функции f2.
        #  Если в первой функции была ошибка, вторая функция должна запуститься.
        #  Сейчас код обрывается и переходит в блок except, если в первой функции получили ошибку.
        if not str(num_x).isdigit() or not str(num_y).isdigit():
            raise ValueError
        res1 = f(int(num_x), int(num_y))
        res2 = f2(int(num_x), int(num_y))
        number = random.randint(0, 100)
        if file_2.closed:
            raise ("result.txt закрыт")
        my_list = sorted([res1, res2, number])
        file_2.write("{} \n".format(' '.join(str(my_list))))
    except ValueError:
        print("Входные данные могут быть только целыми числами")
    file.close()
    file_2.close()


    # TODO, если при открытии файла поймаем ошибку, в таком случае получим ошибку в этом месте.
    #  Возможно лучше создавать/открывать файл тоже до блока try.


#  отредактировать и исправить программу
