res = [x for x in range(2, 1000) if not [y for y in range(2, x) if not x % y]]
res1 = []
for number in range(2, 1000):
    for x in range(2, number):
        if number % x == 0:
            break
    else:
        res1.append(number)
print(res)
print(res1)

# TODO, таким образом, мы использовали способы, которые знали до текущего урока =)
#  Предлагаю добавить в решение функции filter, map и lambda и попробовать решить задание без вложенных циклов.
