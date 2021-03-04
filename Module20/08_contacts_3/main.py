

phonebook = {
    1: { "Имя" : "Иван",
         "Фамилия" : "Сидоров",
         "Номер" : 899999999
    },
    2 : { "Имя" : "Руслан",
          "Фамилия" : "Петров",
          "Номер" : 89995659
    },
}

while True:
    print("1 - Что бы добавить контакт, 2 - Найти контакт по фамилии")
    answer = int(input())
    if answer == 1:
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        tel = int(input("Введите номер телефона: "))
        id = len(phonebook) + 1
        phonebook[id] = {"Имя" : name,
                         "Фамилия" : surname,
                         "Номер" : tel}
    if answer == 2:
        answer = input("Введите фамилию для поиска: ").capitalize()
        for  i_key, i_value in phonebook.items():
            if answer == phonebook[i_key]["Фамилия"]:
                contact = phonebook[i_key]
                print(contact["Имя"], contact["Фамилия"], contact["Номер"])