first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))

print(f"Года от {first_year} до {second_year} с тремя одинаковыми цифрами: ")

for year in range(first_year, second_year + 1):
    remains = ""
    i = 1
    i_1 = 1
    remains_1 = ""
    for symbol in str(year):
        if remains == symbol:
            i += 1
            continue
        elif remains_1 == symbol:
            i_1 += 1
            continue
        elif remains == "":
            remains = symbol
        else:
            remains_1 = symbol

    if i >= 3 or i_1 >= 3:
        print(year)

# зачёт!
