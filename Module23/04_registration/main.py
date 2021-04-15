def chek(data):
    try:
        name, mail, age = i_line.split()
    except ValueError:
        registrations_bad.write(i_line)
        print("НЕ присутствуют все три поля")
    try:
        if not str(name).isalpha():
            registrations_bad.write(i_line)
            raise NameError
        if "@" and "." not in mail:
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
    chek(i_line)
registrations_good.close()
registrations_bad.close()
registration_file.close()

