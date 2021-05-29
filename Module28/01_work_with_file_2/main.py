

class Manager_file:
    # , стоит запрашивать дополнительно "режим" для открытия файла.
    def __init__(self, path: str, metod: str)-> None:
        self.name = path
        self.metod = metod

    def __enter__(self):
        # , предлагаю попробовать ловить ошибки.
        #  К примеру, если пользователь некорректно указал "режим", то пытаться открыть файл насильно любым способом.
        #  Например, при помощи "w".
        try:
            self.file = open(self.name, self.metod)
        except:  # Правильно except Exception.
            self.file = open(self.name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO, стоит ловить ошибки.
        #  Если поймали, то пробуем закрыть файл и возвращаем Истину =)
        if exc_type:
            print(exc_type)
        self.file.close()
        return True


with Manager_file("text.txt", "w") as file:
    file.eror("Hello ")  # TODO как правильно произвести запись в файл?
