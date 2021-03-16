def min_len(object1, object2):
    return min(len(object1), len(object2))


def generator(object1, object2):
    result = ((object1[i_elem], object2[i_elem]) for i_elem in range(min_len(object1, object2)))
    return result


# def print_res_gen (object):


my_list = [3, 5, 6, 1, 5]
my_tupl = (5, 4, 3, 7)
my_string = "avddgddfd"

result = generator(my_list, my_string)
# print_res_gen(result)
print(result)
for sym in result:
    print(sym)

# , пожалуйста, поправьте названия переменных и функций.
#  1. Названия должны отражать суть содержания переменных.
#  2. Функция называется max_len, но возвращает минимальное число =)
#  3. str использовать нельзя, т.к. в python есть функция с таким названием.

# зачёт!
