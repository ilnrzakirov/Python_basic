games = int(input("Сколько записей вносится в протокол: "))
games_result_dict = dict()

print("Записи (результат и имя")
for i_game in range(1, games +1):
    print("{} запись:".format(i_game), end=" ")
    points, player = input().split()
    if player in games_result_dict:
        if games_result_dict[player][0] < points:
            games_result_dict[player] = points, i_game
    else:
        games_result_dict[player] = points, i_game

print("Итоги соревнования: ")

for winner in range (1, 4):
    print("{} место: ".format(winner), end=" ")
    for name, item in games_result_dict.items():





print(games_result_dict)