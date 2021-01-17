first_list = [1, 4, -3, 0, 10, -125, -500, 17]  # TODO, добавил элементы в список и работать перестало =)
min_list = min(first_list)
items = len(first_list)
flag = False  # TODO, переменная лишняя


def sort(first_list):
    for number in range(len(first_list) - 1):
        first_item = first_list[number]
        sescond_item = first_list[number + 1]
        if first_item > sescond_item:
            first_list[number], first_list[number + 1] = first_list[number + 1], first_list[number]
    return first_list


first_list = sort(first_list)

while flag != True:  # TODO, лучше без переменной.
    item = first_list[1]
    res = 0
    for number in first_list[:-2]:
        # Почем после цикла вайл программа снова запускает сортировку!
        if item >= number:  # TODO, видимо из-за этого условия. Оно не срабатывает и мы переходим в else.
            item = first_list[number + 2]
            res += 1
        else:
            first_list = sort(first_list)
            res = 0
        if res == len(first_list) - 2:
            flag = True
            break

print(first_list)
