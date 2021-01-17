n = int(input("Введите количество клеток: "))
cells = []
marriage = ""

for num in range(0, n):
    print(f"Эффективность {num + 1} клетки:", end=" ")
    cells.append(int(input()))
    if num > cells[num]:
        marriage += " " + str(cells[num])
print(f"Неподходящие значения: {marriage}")

# зачёт!
