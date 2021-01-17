word = input("Введите слово: ")
letters = []
similar =[]
n = len(word)
result = []
for symbol in word:
    letters.append(symbol)

for item in range (n - 1):
    for symbol in range (item + 1, n):
        if letters[item] == letters [symbol]:
            similar.append(letters[item])
            break

for item in letters:
    if item not in similar:
        result.append(item)


print(f"Количество уникальных букв: {len(result)}")
