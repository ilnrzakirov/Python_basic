n = int(input("Введите число : "))

# , пожалуйста поправьте нейминг. Пока что не очень ясно, что значит переменная "i".
def summ(number):
    result = 0
    while number != 0:
        remains = number % 10
        result += remains
        number //= 10
    print(f"Сумма чисел: {i}")
    return result


def quantity(number):
    result = 0
    while number != 0:
        result += 1
        number //= 10
    print(f"Количесвто цифр в числе: {i}")
    return result


summ = summ(n)
quantity = quantity(n)
print(f"Разность суммы и количества цифр : {summ - quantity}")

# TODO, пока что при запуске кода ошибка
#  NameError: name 'i' is not defined