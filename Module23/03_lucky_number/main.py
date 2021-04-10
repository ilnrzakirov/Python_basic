summ = 0
count = 0

res_file = open("res.txt", "a")
try:
    while summ < 777:
        number = int(input("Введите число: "))
        count += 1
        if count == 13:
            raise Exception # TODO, возможно, лучше добавить
# TODO, предлагаю попробовать открывать файл до блока try =)
        res_file.write("{} \n".format(str(number)))
        summ += number
except:
    print("Случайная ошибка")
finally:
    res_file.close()
