people = int(input("Количество человек: "))
counting = int(input("Какое число в считалке: "))
print(f"Значит выбывает кадждый {counting} человек")

people_list = list(range(1, people + 1))
start = 0
chek = 0
remains = 0
remains1 = 0
prev = 0

while people != 1:
    print(f"Текущий круг людей: {people_list}")
    if start >= people:
        start = start - people
        prev = start
    print(f'Начало счета с номера {people_list[start]}')
    start += people
    while start >= people:
        if people <= counting:
            start = counting % people - 1 + prev
        else:
            start = people % counting - 1 + prev
    print(f'Выбал игрок под номером {people_list[start]}')
    chek = people_list[start]
    prev = start
    people_list.remove(chek)
    people -= 1

print(f"Остался человек под номером {people_list[0]}")









