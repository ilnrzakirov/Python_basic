def chekchild(dict_parent, all_dict):
    child = []
    for name in dict_parent:
        for i_name in all_dict:
            if name == i_name:
                for human in all_dict[i_name]:
                    child.append(human)
    return child


people = int(input("Введите количество человек: "))


# TODO, по идее, список лишний.
chaild = []
famaly_dict = dict()
for human in range(1, people):
    pair = input("{} пара: ".format(human)).split()
    # TODO получить сразу 2 переменные при split можно, если укажем слева от "=" сразу 2 названия переменных.
    #  pair, second_pair = input(...)
    # TODO, предлагаю сразу добавлять в словарь значение по ключу. Список с проверкой не нужен =)
    #  Возможно, исходя из текущих рекомендаций, сможем упростить код ниже =)
    chaild.append(pair[0])
    if pair[1] in famaly_dict:
        famaly.append(pair[0])
    else:
        famaly = famaly_dict[pair[1]] = []
        famaly.append(pair[0])



for name in famaly_dict:
    if name not in chaild:
        parent = name

height = dict()
height[0] = []
height[0].append(parent)
height[1] = famaly_dict[parent]
height[2] = chekchild(famaly_dict[parent], famaly_dict)
for shift in range(3, len(famaly_dict)):
    height[shift] = chekchild(height[shift - 1], famaly_dict)

famaly_dict.clear()

for i_height in height:
    for elements in height[i_height]:
        famaly_dict[elements] = i_height

for name in sorted(famaly_dict.keys()):
    print(name, famaly_dict[name])
