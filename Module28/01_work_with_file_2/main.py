

class Manager_file:
    def __init__(self, path: str)-> None:
        self.name = path

    def __enter__(self):
        self.file = open(self.name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return True


with Manager_file("text.txt") as file:
    file.write("Hello ")
