number = int(input("Введите длину списка: "))

number_list = [(1 if x % 2 == 0 else x % 5) for x in range(number)]
print(f"Результат {number_list}")

# зачёт!
