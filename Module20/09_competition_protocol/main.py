def keyFunc (item):
    return int(item[1][0])

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
games_result_list = list(games_result_dict.items())

# TODO, т.к. результат храним в тексте, отсортировали некорректно
#  5 запись: 197128 qwerty. Должен быть на 1 месте. У нас на первых местах получились игроки с результатом 95715
# [('Jack', ('95715', 6)), ('qwerty', ('95715', 2)), ('Alex', ('95715', 3)), ('M', ('95715', 9))]

games_result_list.sort(key=keyFunc, reverse=True)
for winner in range (1, 4):
    print("{} место. {} {}".format(winner, games_result_list[winner - 1][0], games_result_list[winner-1][1][0]))

print(games_result_list)

# TODO, sorted лишняя функция пока что =)
#  Предлагаю, после того, как создали список, применить к списку метод .sort()
#  В параметр key метода sort можно добавить параметр сортировки. А так же воспользоваться параметром reverse.



# TODO, давайте попробуем создать список без цикла, применив list к games_result_dict.items() =)
#  После этого, применим в списку функцию для сортировки списка.
#  И далее используем цикл для вывода значение =)

# TODO, далее, необходимо создать список списков из ключей и значений словаря games_result_dict.
#  Поможет функция list и метод словарей items.
#  После этого, сможем просто пройти по списку в цикле =)