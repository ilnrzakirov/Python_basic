def fibonachi(num_pos, chek=2, start=0, res=1):
    # , Предлагаю упростить решение.
    #  Нужен только 1 параметр функции =)
    #  Нам необходимо просто вернуть сумму чисел предыдущего числа и предпредыдущего =)
    if num_pos == 1:  # , если 2, тоже необходимо выйти из рекурсии
        return 1
    if chek == num_pos:
        return res + start
    chek += 1
    result = res + start
    start = res
    return fibonachi(num_pos, chek, start, result)


def fibonachi2(num_pos):
    if num_pos == 1 or num_pos == 2:
        return 1
    result = fibonachi2(num_pos - 2) + fibonachi2(num_pos - 1)
    return result


num_pos = int(input("Введите номер позиции: "))

print(fibonachi2(num_pos))

# зачёт!
