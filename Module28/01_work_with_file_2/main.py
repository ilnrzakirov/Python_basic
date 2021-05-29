

class Manager_file:
    # TODO, стоит запрашивать дополнительно "режим" для открытия файла.
    def __init__(self, path: str)-> None:
        self.name = path

    def __enter__(self):
        # TODO, предлагаю попробовать ловить ошибки.
        #  К примеру, если пользователь некорректно указал "режим", то пытаться открыть файл насильно любым способом.
        #  Например, при помощи "w".
        self.file = open(self.name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO, стоит ловить ошибки.
        #  Если поймали, то пробуем закрыть файл и возвращаем Истину =)

        if self.file:
            self.file.close()
        return True


with Manager_file("text.txt") as file:
    file.write("Hello ")
