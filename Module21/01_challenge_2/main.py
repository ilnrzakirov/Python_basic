def output_num(num):  # TODO, возможно параметр step лишний
    if num == 0:
        return 1
    print(num)
    return output_num(num -1)

# TODO, число пользователя пока что не выводится, но тоже должно =)
num = int(input("Введите число: "))
numm = output_num(num)
