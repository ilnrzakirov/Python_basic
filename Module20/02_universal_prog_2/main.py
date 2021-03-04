def is_prime (number):
    chek = True
    for num in range (2, number -1):
        if number % num == 0:
            chek = False
    return chek

def result_list (object):
    result = []
    for i_object, value in enumerate(object):
        if is_prime(i_object):
            result.append(value)

    return result

