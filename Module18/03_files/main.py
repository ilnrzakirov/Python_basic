file_name = input("Введите название файла: ")
bad_start = ("@", "№", "$", "%", "^", "&", "*", "(", ")")
allowed_end = (".txt", ".docx")
if file_name.startswith(bad_start):
    print("Название файла начинается на одно из запрещенных символов")
elif not file_name.endswith(allowed_end):
    print("Неверное расширение файла")
else:
    print("Фаайл назван правильно")

#про кортежи тоже прочел в описании метода