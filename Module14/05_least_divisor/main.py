n = int(input("Введите число: "))

def divider (n):
    result = 0
    for number in range (2, n + 1):
        if n % number == 0:
            result = number
            break
    print(f"Наименьший делитель, отличный от единицы: {result}")



if n <= 1:
    print("Число меньше или равно единицы")
else:
    divider (n)