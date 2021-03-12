def output_num (num, step = 1):
    if step == num:
        return 1
    print(num - (num - step))
    return output_num(num, step +1)






numm = output_num(5)
