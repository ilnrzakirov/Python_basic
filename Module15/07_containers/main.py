n = int(input("Введите количество контейнеров: "))
container = []
result = 0
for num in range (1, n +1):
    container.append(int(input("Введите вес контейнера: ")))

new_container = int(input("Введите вес нового контейнера: "))

for item in container:
    result += 1
    if new_container > item:
        break
    if result == len(container):
        result +=1
        break

print(result, container)