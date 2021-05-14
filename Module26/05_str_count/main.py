import os


def code_counter():
    directory = os.getcwd()
    for path in os.walk(directory):
        if str(path).endswith(".py"):
            with open(str(path), "r") as file:
                global result
                for line in file:
                    if line.split() != []:
                        result += 1
    return result


result = 0
print(code_counter())
