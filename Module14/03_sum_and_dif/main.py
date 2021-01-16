n = int(input("Введите число : "))

def summ (number):
    i = 0
    while number !=0:
        remains = number % 10
        i += remains
        number //= 10
    print(f"Сумма чисел: {i}")
    return i

def quantity (number):
    i = 0
    while number != 0:
        i += 1
        number //= 10
    print(f"Количесвто цифр в числе: {i}")
    return i
summ = summ(n)
quantity = quantity(n)
print(f"Разность суммы и количества цифр : {summ - quantity}")
