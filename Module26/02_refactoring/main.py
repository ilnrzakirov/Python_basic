from collections.abc import Iterable

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def gen(list1: list, list2: list, number: int) -> Iterable[str]:  # , вместо None лучше Iterator[str].
    for x in list1:
        for y in list2:
                         # , возврат получился лишний
            if x * y == number:
                yield x * y # , в этом месте стоит возвращать результат при помощи yield


result = gen(list_1, list_2, to_find)
for item in result:
    print(item)

# can_continue = True
# for x in list_1:
#    for y in list_2:
#        result = x * y
#        print(x, y, result)
#        if result == to_find:
#            print('Found!!!')
#            can_continue = False
#            break
#    if not can_continue:
#        break

# TODO провести рефакторинг кода
