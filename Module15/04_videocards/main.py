n = int(input("Введите количество видекарт: "))
video_card = []
new_list_video_card = []

for num in range(n):
    print(f"{num + 1} Видеокарта: ", end=" ")
    video_card.append(int(input()))

max_video_card = max(video_card)

for number in video_card:
    if max_video_card != number:
        new_list_video_card.append(number)

print(f"Старый список видео карт {video_card}")
print(f"Новый список видео карт {new_list_video_card}")

