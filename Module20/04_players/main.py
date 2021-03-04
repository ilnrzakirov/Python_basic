players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_list = []
player = []
for i_key, i_value in players.items():
    for item in i_key:
        player.append(item)
    for item in i_value:
        player.append(item)
    player_tuple = tuple(player)
    players_list.append(player_tuple)
    player =[]


#players_list = [item for item in players.items()]
print(players_list)