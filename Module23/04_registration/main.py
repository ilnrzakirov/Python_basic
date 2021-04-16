def chek(data):
    # , функция должна работать с data, а не с i_line =)
    #  т.к. data это параметр функции, а i_line это внешняя переменная.

        # , предлагаю проверять, если split не состоит из 3х элементов,
        #  то, выбрасывать ошибку.
    if len(data.split()) != 3:
        raise ValueError ("НЕ присутствуют все три поля")
    name, mail, age = data.split()
    if not str(name).isalpha():
        raise NameError ("поле имени содержит НЕ только буквы")
            # , таким образом можно вызывать ошибку с определённым текстом NameError("Текст ошибки")
            #  В таком случае, ошибки можно будет ловить группой.
    if "." not in mail or "@" not in mail: # , таким образом наличие "@" в mail не проверяем.
            raise SyntaxError ("поле емейл НЕ содержит @ и .(точку)")
    if 10 > int(age) > 99:
            raise ValueError ("поле возраст НЕ является числом от 10 до 99")


registration_file = open("registrations.txt", "r", encoding="UTF-8")
registrations_good = open("registrations_good.log", "a", encoding="UTF-8")
registrations_bad = open("registrations_bad.txt", "a", encoding="UTF-8")
for i_line in registration_file:
    # , ловить ошибки и записывать их в файл предлагаю в основном цикле нашей программы.
    #  В этом месте. Но вызывать внутри функции.
    # Я не понял, как это вызывать внутри функции а ловить здесь? Блок try не нужен? просто raise?
    try:
        chek(i_line)
        registrations_good.write(i_line)
    except (ValueError, NameError, SyntaxError) as err:
        # TODO, предлагаю добавить синоним "as err" и записывать в файл не только строку, но и тип ошибки.
        #  Возможно, стоит добавить символ переноса строки при записи.
        registrations_bad.write("{}:{}".format(err, i_line))




registrations_good.close()
registrations_bad.close()
registration_file.close()

