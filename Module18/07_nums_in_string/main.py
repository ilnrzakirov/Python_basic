text = input("Введите строку: ")

res = [int(number) for number in text if number.isdigit() ]
result = "".join(str(res))

print(result)

