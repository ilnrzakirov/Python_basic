import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    # TODO, в наших функциях не нужно вызывать исключения.
    #  Выпадут сами, если делитель будет равен "0"
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x



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
    file.close()
    file_2.close()
except FileNotFoundError:
    print("Что-то пошло не так")
    # TODO, если при открытии файла поймаем ошибку, в таком случае получим ошибку в этом месте.
    #  Возможно лучше закрывать файл тоже в блоке try.


#  отредактировать и исправить программу
