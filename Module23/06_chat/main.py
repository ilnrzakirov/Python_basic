
text_file = open("chat.txt", "a+", encoding="UTF-8")

user = input("Введите имя пользователя: ")

while True:
    answer = input("Посмотреть текущий чат - 1, отправить сообщение - 2: ")
    try:
        if int(answer) == 1:
            text_file.seek(0)
            for i_line in text_file.readlines():
                print(i_line)
        if int(answer) == 2:
            message = input("Введите сообщение: ")
            text_file.write('{}: {} \n'.format(user, message))
        if int(answer) != 1 and int(answer) != 2:
            raise ValueError
    except ValueError:
        print("Такого варианта собыйтий нет")

