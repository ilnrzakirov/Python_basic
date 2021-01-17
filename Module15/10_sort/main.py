first_list = [10, 4, -3, -5, 8, -7, 5, 1, 9, -18, -500, 127, -198]
min_list = min(first_list)
items = len(first_list)


def sort(first_list):
    for number in range(len(first_list) - 1):
        first_item = first_list[number]
        sescond_item = first_list[number + 1]
        if first_item > sescond_item:
            first_list[number], first_list[number + 1] = first_list[number + 1], first_list[number]
    return first_list


first_list = sort(first_list)
res = 0

while res < len(first_list) - 2:
    item = first_list[1]
    res = 0
    for number in first_list[:-2]:
        if item >= number:
            item = first_list[res + 2]
            res += 1
        else:
            first_list = sort(first_list)
            res = 0
            break
        if res == len(first_list) - 2:
            flag = True
            break

print(first_list)

# зачёт!
