def chek(data):
    # TODO, функция должна работать с data, а не с i_line =)
    #  т.к. data это параметр функции, а i_line это внешняя переменная.
    try:
        # TODO, предлагаю проверять, если split не состоит из 3х элементов,
        #  то, выбрасывать ошибку.
        if data.split() != 3:
            raise ValueError
        name, mail, age = data.split()
    except ValueError:
        registrations_bad.write(data)
        print("НЕ присутствуют все три поля")
    try:
        if not str(name).isalpha():
            registrations_bad.write(data)
            raise NameError ("поле имени содержит НЕ только буквы")
            # TODO, таким образом можно вызывать ошибку с определённым текстом NameError("Текст ошибки")
            #  В таком случае, ошибки можно будет ловить группой.
        if "." not in mail or "@" not in mail: # TODO, таким образом наличие "@" в mail не проверяем.
            registrations_bad.write(data)
            raise SyntaxError ("поле емейл НЕ содержит @ и .(точку)")
        if 10 > int(age) > 99:
            registrations_bad.write(data)
            raise ValueError ("поле возраст НЕ является числом от 10 до 99")
        registrations_good.write(data)
    except (NameError, SyntaxError, ValueError):
        print("Какая то ошибка")






registration_file = open("registrations.txt", "r", encoding="UTF-8")
registrations_good = open("registrations_good.log", "a", encoding="UTF-8")
registrations_bad = open("registrations_bad.log", "a", encoding="UTF-8")
for i_line in registration_file:
    # TODO, ловить ошибки и записывать их в файл предлагаю в основном цикле нашей программы.
    #  В этом месте. Но вызывать внутри функции.
    # Я не понял, как это вызывать внутри функции а ловить здесь? Блок try не нужен? просто raise?
    chek(i_line)
registrations_good.close()
registrations_bad.close()
registration_file.close()

