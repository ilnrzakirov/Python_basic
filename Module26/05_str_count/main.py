import os


def code_counter():
    directory = os.getcwd() # директория для подсчета
    for path in os.listdir(directory):
        new_path = directory + "".join(path)
        if str(new_path).endswith(".py"):
            with open(str(path), "r") as file:
                global result
                for line in file:
                    if line.split() != []:
                        result += 1
    return result


result = 0
print(code_counter())
