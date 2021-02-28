orders = int(input("Введите количество заказов: "))
orders_dict = dict()

for i_order in range(1, orders + 1):
    print("{} заказ:".format(i_order), end=" ")
    order = input().split()
    if order[0] not in orders_dict:
        order_name = orders_dict[order[0]] = [{}]
    else:
        order_name = orders_dict[order[0]]
    if order[1] in order_name[0]:
        order_name[0][order[1]] += int(order[2])
    else:
        order_name[0][order[1]] = int(order[2])

for name in orders_dict:
    print(name)
    for elements in orders_dict[name][0]:
        print("\t\t", elements, ":", orders_dict[name][0][elements])

# зачёт!
