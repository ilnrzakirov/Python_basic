
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


