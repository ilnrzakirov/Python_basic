total_sym = 0
line_count = 0
people_name = open("people.txt", "r", encoding="UTF-8")
errors = open("errors.log", "a", encoding="UTF-8")

# , создавать/открывать файл для записи ошибок предлагаю до блока try/except.
for i_line in people_name:
    # , стоит ловить ошибки внутри цикла. Иначе, если в цикле возникает ошибка,
    #  Из цикла выходим.
    try:
        len_line = len(i_line)
        line_count += 1
        if i_line.endswith("\n"):
            len_line -= 1
        if len_line < 3:
            #  записывать ошибки в файл предлагаю в блоке except
            raise Exception  # , возможно, лучше использовать Exception
        total_sym += len_line

    except Exception:
        error = "Длина {} строки меньше трех символов \n".format(line_count)
        errors.write(error)
        print("Длина {} строки меньше трех символов".format(line_count))
#    finally:
#        print("Количество символов: {}".format(total_sym))
        # таким образом файл закрывается после первой итерации цикла, но не должен.
print("Количество символов: {}".format(total_sym))
people_name.close()

# , если получили ошибку, код не должен прекратить работу.
