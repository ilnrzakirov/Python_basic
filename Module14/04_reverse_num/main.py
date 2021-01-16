n = float(input("Введите первое число: "))
k = float(input("Введите второе число: "))


def reflect(number):
    intg = ""
    fract = ""
    i = False
    remains = ""
    remains_1 = ""
    for symbol in str(number):
        if symbol == ".":
            num1 = intg
            i = True
            continue
        intg += symbol
        if i != False:
            fract += symbol
    while int(num1) != 0:
        k = int(num1) % 10
        remains += str(k)
        num1 = int(num1) // 10
    while int(fract) != 0:
        k = int(fract) % 10
        remains_1 += str(k)
        fract = int(fract) // 10
    result = str(remains) + "." + str(remains_1)
    return result


n_1 = reflect(n)
k_1 = reflect(k)

print(f"Первое число наоборот: {n_1}")
print(f"Второе число наоборот: {k_1}")
print(f"Сумма: {float(n_1) + float(k_1)}")


# зачёт!