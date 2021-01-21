violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
total_time = 0
songs = int(input("Сколько песен выбрать?"))

for i_team in range (songs):
    print(f"Название {i_team + 1} песни: ", end=" ")
    song = input()
    for iteam in violator_songs:
        for i_song in iteam:
            if i_song == song:
                total_time += iteam[1]
print(f"Общее время звучания песен {round(total_time, 2)}")


