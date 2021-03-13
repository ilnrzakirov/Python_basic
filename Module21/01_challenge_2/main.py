def output_num(num, step=1):  # TODO, возможно параметр step лишний
    if step == num:
        return 1
    print(num - (num - step))
    return output_num(num, step + 1)

# TODO, число пользователя пока что не выводится, но тоже должно =)
numm = output_num(5)
