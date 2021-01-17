n = int(input("Введите число: "))
number_list =[]

for number in range (1, n + 1):
    if number % 2 == 0:
        number_list.append(number)

print(number_list)

# TODO Напишите программу, которая формирует список из нечетных чисел от 1 до N.
#  Введите число: 11
#  [2, 4, 6, 8, 10]
#  Пока что все числа чётные. Должны закончить числом 11 =)
