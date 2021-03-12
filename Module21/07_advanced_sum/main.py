def summ (object, result= 0):
    for item in object:
        if isinstance(item, list):
            result += summ(item, result=0)
        else:
            result += item
    return result


my_list = [1, 2, 3, [5], 8, [1, 2]]
print(summ(my_list))