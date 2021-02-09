y = input("По оси ОУ: ")
x = input("По оси ОХ: ")

if y.startswith("South"):
    y_list = y.split(" ")
    coordinate_y = "-" + str(y_list[1])
else:
    remains = y.index(" ")
    coordinate_y = y[remains + 1:]

if x.startswith("East"):
    remains1 = x.index(" ")
    coordinate_x = x[remains1 + 1:]
else:
    x_list = x.split(" ")
    coordinate_x = "-" + str(x_list[1])

print("Координаты {} {}".format(coordinate_x, coordinate_y))

# зачёт!
