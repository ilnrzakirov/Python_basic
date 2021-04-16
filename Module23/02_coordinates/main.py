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
    # , стоит ловить ошибки в цикле, иначе, программа завершает свою работу наткнувшись на ошибку в цикле.
    num_x, num_y = line.split()
    #  проверки ниже получились лишние.
    #  В данном задании нем не нужно вызывать ошибки, только ловить их.
    #  Предлагаю сначала ловить ошибку функции f, после этого ловить ошибку в функции f2.
    #  Если в первой функции была ошибка, вторая функция должна запуститься.
    #  Сейчас код обрывается и переходит в блок except, если в первой функции получили ошибку.
    try:
        res1 = f(int(num_x), int(num_y))
    except:
        print("Ошибка в функции f")

    try:
        res2 = f2(int(num_x), int(num_y))
    except:
        print("Ошибка в функции f2")
    number = random.randint(0, 100)
    #  было бы здорово поймать и эту ошибку =)
    #  NameError: name 'res1' is not defined
    #  Возникает, если одна из функций возвращает ошибку.
    try:
        my_list = sorted([res1, res2, number])
    except NameError:
        print("Что то пошло не так")
    file_2.write("{} \n".format(' '.join(str(my_list))))
file.close()
file_2.close()

#  если при открытии файла поймаем ошибку, в таком случае получим ошибку в этом месте.
#  Возможно лучше создавать/открывать файл тоже до блока try.


#  отредактировать и исправить программу
