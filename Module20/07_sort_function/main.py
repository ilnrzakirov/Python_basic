def sort(sort_tuple):
    for item in sort_tuple:
        # TODO, возможно стоит проверить тип элемента при помощи isinstance?
        if not str(item).isdigit():
            return sort_tuple
    # TODO, возможно, весь остальной код лишний =)
    #  Можно применить в sort_tuple функцию sorted и вернуть =)
    sort_tuple = list(sort_tuple)
    chek = True
    while chek:
        cnt = 0
        for i_item, item in enumerate(sort_tuple):
            if i_item == len(sort_tuple) - 1:
                break
            if item > sort_tuple[i_item + 1]:
                sort_tuple[i_item], sort_tuple[i_item + 1] = sort_tuple[i_item + 1], sort_tuple[i_item]
        for i_item, item in enumerate(sort_tuple):
            if i_item == len(sort_tuple) - 1:
                break
            if item < sort_tuple[i_item + 1]:
                cnt += 1
            if cnt == len(sort_tuple) - 1:
                chek = False

    return sort_tuple


# my_tuple = (5, 4, 2, 6, 11, 9, 1)
# TODO, пока что не сортируем элементы =)
my_tuple = (6, 3, -1, 8, 4, 10, -5)
print(sort(my_tuple))
