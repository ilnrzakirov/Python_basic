skates = int(input("Количество коньков: "))
all_skates = []
result = 0

for number in range(skates):
    print(f"Размер {number + 1} пары: ", end=" ")
    skate = int(input())
    all_skates.append(skate)

people = int(input("Количество людей: "))

for number in range(people):
    print(f"Размер ноги {number + 1} человека: ", end=" ")
    size = int(input())
    for i_team in all_skates:
        if size <= i_team:
            result += 1
            all_skates.remove(i_team)
            break

print(f"Наибольшее количество людей, которые могут взять ролики: {result} ")

# зачёт!
