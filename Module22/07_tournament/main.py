
input_file = open("first_tour.txt", 'r')
k = input_file.read().split()[:1]
points_second_tour = int(k[0])
input_file.seek(4)
winer_dict = dict()

# отбор участников с очками более k и составление словаря победителей
for i_line in input_file.readlines():
    # TODO, для коаращения количества срещов в коде, предлагаю сразо создавать 3 переменные вместо 1 списка =)
    # TODO, по идее, так много циклов нам не нужно.
    #  ммы можем идти в цикле по 1 файлу и сразу записывать данные в другой, в случае,
    #  если победитель проходит по количеству балов.
    player_list = i_line.split()
    if int(player_list[2]) > points_second_tour:
        for i_sym, sym in enumerate(player_list[0]):
            if i_sym ==0:
                name_string = sym + "."
        name = name_string + player_list[1]
        winer_dict[name] = player_list[2]

output_file = open("second_tour.txt", "a")
# Запись количество побдителей в файл
player_count = str(len(winer_dict)) + "\n"
output_file.write(player_count)

# запись в файл результатов победителей
for name, points in winer_dict.items():
    # TODO, запись в файл возможно стоит сделать без дополнительной переменной
    #  При помощи форматирования строк =)
    player_result = name + " " + str(points)+ "\n"
    output_file.write(player_result)

input_file.close()
output_file.close()
