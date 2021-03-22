zen = open("zen.txt", "r")

for i_line in reversed(zen.readlines()):
    print(i_line, end="")

zen.close()

# зачёт!
