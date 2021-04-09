total_sym = 0
line_count =0

try:
    people_name = open("people.txt", "r", encoding="UTF-8")
    errors = open("errors.log", "a", encoding="UTF-8")
    for i_line in people_name:
        len_line = len(i_line)
        line_count += 1
        if i_line.endswith("\n"):
            len_line -= 1
        if len_line < 3:
            error = "Длина {} строки меньше трех символов \n".format(line_count)
            errors.write(error)
            raise BaseException ("Длина {} строки меньше трех символов".format(line_count))
        total_sym += len_line
    people_name.close()
except FileNotFoundError:
    errors.write("Файл не найден")
    print("Файл не найден")
finally:
    print("Количество символов: {}".format(total_sym))
