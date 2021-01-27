word = input("Введите текст: ")
word1 = word[::-1]
a = word.index("h")
b = word1.index("h")
print(word[len(word) - b - 2 : a: -1])
print(a, b)

