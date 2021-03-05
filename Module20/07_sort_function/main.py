def sort(sort_tuple):
    if not isinstance(sort_tuple, tuple):
        #    for item in sort_tuple:
        # , возможно стоит проверить тип элемента при помощи isinstance?
        #        if not str(item).isdigit():
        return sort_tuple
    # , возможно, весь остальной код лишний =)
    #  Можно применить в sort_tuple функцию sorted и вернуть =)
    else:
        return sorted(sort_tuple)


# my_tuple = (5, 4, 2, 6, 11, 9, 1)
# , пока что не сортируем элементы =)
my_tuple = (6, 3, -1, 8, 4, 10, -5)
print(sort(my_tuple))

# зачёт!
