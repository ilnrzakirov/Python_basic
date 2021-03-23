
input_file = open("first_tour.txt", 'r')
k = input_file.read().split()[:1]
points_second_tour = k[0]
input_file.seek(4)
winer_dict = dict()

for i_line in input_file.readlines():
    player_list = i_line.split()
    if int(player_list[2]) > 80:
        for i_sym, sym in enumerate(player_list[0]):
            if i_sym ==0:
                name_string = sym + "."
        name = name_string + player_list[1]
        winer_dict[name] = player_list[2]

output_file = open("second_tour.txt", "a")
player_count = str(len(winer_dict)) + "\n"
output_file.write(player_count)

for name, points in winer_dict.items():
    player_result = name + " " + str(points)+ "\n"
    output_file.write(player_result)

input_file.close()
output_file.close()
