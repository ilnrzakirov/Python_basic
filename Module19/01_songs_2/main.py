violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

total_t = 0
songs = int(input("Сколько песен выбрать? "))
# , как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
for i_song in range(1, songs + 1):
    song = input("Название {} песни: ".format(i_song))
    if song in violator_songs:
        total_t += violator_songs[song]
    else:
        print("Песня отсутсвует в списке ")
print("Общее время звучания песен: {}".format(total_t))

# зачёт!
