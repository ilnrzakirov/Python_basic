nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# TODO, пожалуйста, придумайте более полное название для переменной.
def exp (lst, result_list = []): # TODO, параметр выгядит лишним. =)
    # TODO, цикл лишний, в нашем случае, цикл заменяет рекурсия.
    for item in lst:
        if isinstance(item, list):
            exp(item)
        else:
            result_list.append(item)
    return result_list


print(exp(nice_list))
