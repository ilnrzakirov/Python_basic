import os

def save_document (string):
    user_path = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел)").split()
#    user_path = ["users", "ilnur", "pycharmprojects", "python_basic", "module22", "05_save"]
    print(user_path)
    path = os.path.abspath(os.path.sep)
    for elem in user_path:
        path = os.path.join(path, elem)
    print(path)
    file_name = input("Введите название файла: ")
#    file_name = "my_document.txt"
    if file_name in os.listdir(path):
        my_file = open(file_name, "w")
        answer = input("Вы действительно хотите перезаписать файл? ").lower()
        if answer =="да":
            my_file.write(string)
            print("Файл успешно перезаписан")
        else:
            print("Данные не сохранены")
        my_file.close()
    else:
        my_file = open(file_name, "w")
        my_file.write(string)
        print("Файл успешно сохранен")


string = "test string"
save_document(string)
