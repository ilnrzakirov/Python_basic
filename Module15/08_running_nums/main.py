shift = int(input("Сдвиг: "))
n = [1, 2, 3, 4, 5]
new_list = []

for symbol in n [:len(n) - shift -1:-1]:
    new_list.append(symbol)

for symbol in n [:len(n) - shift ]:
    new_list.append(symbol)

print(new_list)