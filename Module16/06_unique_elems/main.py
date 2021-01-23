first_list = []
second_list = []


def list_gen(stop, sl):
    for number in range(stop):
        sl.append(int(input("Введите число: ")))


list_gen(3, first_list)
list_gen(7, second_list)

first_list.extend(second_list)


def chek(sl, item):
    repit = sl.count(item)
    return repit


for item in range(1, 10):
    a = chek(first_list, item)
    while a > 1:
        first_list.remove(item)
        a -= 1

print(first_list)

# зачёт!
