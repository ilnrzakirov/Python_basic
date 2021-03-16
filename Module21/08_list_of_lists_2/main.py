nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# , пожалуйста, придумайте более полное название для переменной.
# def exp_list (input_list, result_list = []): # , параметр выгядит лишним. =)
#    # , цикл лишний, в нашем случае, цикл заменяет рекурсия.
#    for item in input_list:
#        if isinstance(item, list):
#            exp_list(item)
#        else:
#            result_list.append(item)
#    return result_list

def exp_list(input_list):
    if input_list == []:
        return input_list
    if isinstance(input_list[0], list):
        return exp_list(input_list[0]) + exp_list(input_list[1:])
    return input_list[:1] + exp_list(input_list[1:])


print(exp_list(nice_list))

# зачёт!
