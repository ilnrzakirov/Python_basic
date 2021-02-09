text = input("Введите строку: ")

result = [int(number) for number in text if number.isdigit() ]

print(str(result).strip('[]'))

# TODO, как реализовать вывод не списком, а строкой?