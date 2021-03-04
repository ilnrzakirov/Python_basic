def sort (sort_tuple):
    for item in sort_tuple:
        if not str(item).isdigit():
            return sort_tuple
    sort_tuple = list(sort_tuple)
    chek = True
    while chek:
        for i_item ,item in enumerate(sort_tuple):
            if i_item == len(sort_tuple)- 1:
                break
            if item > sort_tuple[i_item + 1]:
                sort_tuple [i_item], sort_tuple [i_item + 1] = sort_tuple [i_item + 1], sort_tuple [i_item]
        # проверка

    return sort_tuple

my_tuple = (5, 4, 2, 6, 11, 9, 1)

print(sort(my_tuple))