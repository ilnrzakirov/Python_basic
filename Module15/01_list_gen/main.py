n = int(input("Введите число: "))
number_list =[]

for number in range (1, n + 1):
    if number % 2 == 0:
        number_list.append(number)

print(number_list)

