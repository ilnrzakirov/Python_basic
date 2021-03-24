input_file = open("first_tour.txt", 'r')
k = input_file.read().split()[:1]
points_second_tour = int(k[0])
input_file.seek(4)
winer_dict = dict()

# отбор участников с очками более k и составление словаря победителей
for i_line in input_file.readlines():
    # , для коаращения количества срещов в коде, предлагаю сразо создавать 3 переменные вместо 1 списка =)
    # , по идее, так много циклов нам не нужно.
    #  ммы можем идти в цикле по 1 файлу и сразу записывать данные в другой, в случае,
    #  если победитель проходит по количеству балов.
    surname_player, name_player, point = i_line.split()
    if int(point) > points_second_tour:
        name_string = name_player[0] + "."
        name = name_string + surname_player
        winer_dict[name] = point

output_file = open("second_tour.txt", "a")
# Запись количество побдителей в файл
player_count = str(len(winer_dict)) + "\n"
output_file.write(player_count)

# запись в файл результатов победителей
for name, points in winer_dict.items():
    # , запись в файл возможно стоит сделать без дополнительной переменной
    #  При помощи форматирования строк =)
    output_file.write(f"{name} {str(points)} \n")

input_file.close()
output_file.close()

# зачёт!
