players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# players_list = []
# player = []


# for i_key, i_value in players.items():
#     for item in i_key:
#         player.append(item)
#     for item in i_value:
#         player.append(item)
#     player_tuple = tuple(player)
#     players_list.append(player_tuple)
#     player = []
# TODO, возможно сможем за 1 генератор списков сделать список множеств типа ('Ivan', 'Volkin', 10, 5, 13) ? =)
#  ПО идее, поправить соввесм немного.

# TODO, совершенно, правильная идея идти по словарю с items.
#  Необходимо разложить i_item на ключ и значение.
#  for key, value in example_dict.items()
#  далее, можно просто сложить ключ и значение =)

players_list = [item
                for i_item in players.items()
                for i in i_item
                for item in i ]
print(players_list)
