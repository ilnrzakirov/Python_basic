n = int(input("Введите количество видекарт: "))
video_card = []
new_list_video_card = []

# , как исправить range таким образом, чтобы не делать вычисления с переменной цикла "num + 1" ? =)
for num in range(1, n + 1):
    print(f"{num} Видеокарта: ", end=" ")
    video_card.append(int(input()))

max_video_card = max(video_card)

for number in video_card:
    if max_video_card != number:
        new_list_video_card.append(number)

print(f"Старый список видео карт {video_card}")
print(f"Новый список видео карт {new_list_video_card}")

# зачёт!
