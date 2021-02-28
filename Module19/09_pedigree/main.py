def chekchild (dict_parent, all_dict ):
    child = []
    for name in dict_parent:
        for i_name in all_dict:
            if name == i_name:
                for human in all_dict[i_name]:
                    child.append(human)
    return child

people = int(input("Введите количество человек: "))

chaild = []
famaly_dict = dict()
for human in range (1, people):
    pair = input("{} пара: ".format(human)).split()
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
height[0] = parent
height[1] = famaly_dict[parent]
height[2] = chekchild(famaly_dict[parent], famaly_dict)
for shift in range (3, len(famaly_dict)):
    height[shift] = chekchild(height[shift -1], famaly_dict)

print(height)


