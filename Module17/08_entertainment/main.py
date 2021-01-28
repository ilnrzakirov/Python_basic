# TODO здесь писать код
n = int(input("Введите количество палочек: "))
stick_list = [x for x in range(1, n + 1)]

throws = int(input("Количество бросков: "))

for i_throws in range (throws):
    print(f"Бросок {i_throws + 1}")
    left = int(input("Сбиты палки с номера  "))
    rigth = int(input("по номер  "))
    for i_border in range (left, rigth + 1):
        stick_list [i_border - 1] = ["."]

for symbol in stick_list:
    if symbol != ["."]:
        ind = stick_list.index(symbol)
        stick_list [ind] = ["|"]


# TODO как вывести результат в формате "Результат: I.....I..." ?


print(stick_list)
