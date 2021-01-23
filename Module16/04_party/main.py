guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
all_guests = 5
answer = ""

while answer != "пора спать":
    print(f"Сейчас на вечеринке {all_guests} человек. {guests}")
    answer = input("Гость пришел или ушел: ")
    if answer == "пришел":
        name = input("Имя гостя: ")
        if all_guests >= 6:
            print(f"Прости, {name}, но мест больше нет")
        else:
            guests.append(name)
            print(f"Привет, {name}")
            all_guests += 1
    elif answer == "ушел":
        all_guests -= 1
        name = input("Имя гостя: ")
        guests.remove(name)
        print(f"Пока, {name}")
    if answer == "пора спать":
        print("Вечеринка закончилась, все легли спать")

# зачёт!
