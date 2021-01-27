all_list = [0, 4, 5, 3, 4, 0, 0, 2, 10]


def appnd(num):
    for _ in range(num):
        all_list1.append(0)


all_list1 = [i_team for i_team in all_list if i_team != 0]
remains = len(all_list) - len(all_list1)
appnd(remains)

print(all_list1)
print(all_list1[:len(all_list1) - remains])

# TODO, у как удалить "0" из списка списковым методом?
