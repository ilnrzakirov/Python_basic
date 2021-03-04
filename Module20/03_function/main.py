def selection (tuple_elements, element):
    new_item_list = []
    chek = False
    for item in tuple_elements:
        if element in new_item_list and item == element:
            new_item_list.append(item)
            break
        if item == element:
            chek = True
        if chek:
            new_item_list.append(item)
    new_item_tuple = tuple(new_item_list)
    return new_item_tuple

tuple_elements = (1, 2, 3, 4, 5, 2, 8)
element = 2
print(selection(tuple_elements, element))

