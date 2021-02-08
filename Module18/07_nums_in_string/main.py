text = input("Введите строку: ")

result = [int(number) for number in text if number.isdigit() ]

print(result)

