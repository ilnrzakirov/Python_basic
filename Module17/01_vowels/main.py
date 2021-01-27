vowels = ["а", "я", "у", "ю", "о", "е", "ы", "и", "э", "ё"]
text = input("Введите текст: ")

vowels_text = [letter for letter in text if letter in vowels]
print(f"Список гласных букв {vowels_text}")
print(f"Длина списка {len(vowels_text)}")


