def is_prime(number):
    for num in range(2, number - 1):
        if number % num == 0:
            return False  # , лучше просто return False
    return True  # , лучше просто return True


def result_list(object):
    result = []
    for i_object, value in enumerate(object):
        if is_prime(i_object):
            result.append(value)

    return result


user = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
print(result_list(user))

# зачёт!
