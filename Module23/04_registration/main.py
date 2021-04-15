def chek(data):
    # TODO, функция должна работать с data, а не с i_line =)
    #  т.к. data это параметр функции, а i_line это внешняя переменная.
    try:
        # TODO, предлагаю проверять, если split не состоит из 3х элементов,
        #  то, выбрасывать ошибку.
        name, mail, age = i_line.split()
    except ValueError:
        registrations_bad.write(i_line)
        print("НЕ присутствуют все три поля")
    try:
        if not str(name).isalpha():
            registrations_bad.write(i_line)
            raise NameError
            # TODO, таким образом можно вызывать ошибку с определённым текстом NameError("Текст ошибки")
            #  В таком случае, ошибки можно будет ловить группой.
        if "@" and "." not in mail: # TODO, таким образом наличие "@" в mail не проверяем.
            registrations_bad.write(i_line)
            raise SyntaxError
        if 10 > int(age) > 99:
            registrations_bad.write(i_line)
            raise ValueError
        registrations_good.write(i_line)
    except NameError:
        print("поле имени содержит НЕ только буквы")
    except SyntaxError:
        print("поле емейл НЕ содержит @ и .(точку)")
    except ValueError:
        print("поле возраст НЕ является числом от 10 до 99")





registration_file = open("registrations.txt", "r", encoding="UTF-8")
registrations_good = open("registrations_good.log", "a", encoding="UTF-8")
registrations_bad = open("registrations_bad.log", "a", encoding="UTF-8")
for i_line in registration_file:
    # TODO, ловить ошибки и записывать их в файл предлагаю в основном цикле нашей программы.
    #  В этом месте. Но вызывать внутри функции.
    chek(i_line)
registrations_good.close()
registrations_bad.close()
registration_file.close()

