import random


def great_list(number_list):
    number_list1 = []
    number_list2 = []
    cnt = 0
    for num in number_list:
        if cnt % 2 == 0:
            number_list1.append(num)
        else:
            number_list2.append(num)
        cnt += 1
    result = zip(number_list1, number_list2)
    return result


def great_list2(num1, num2):
    return num1, num2


number_list = [random.randint(0, 50) for _ in range(10)]
result = list(great_list(number_list))
print(result)

result1 = []
for i_num, num in enumerate(number_list):
    if i_num % 2 == 0:
        result1.append(great_list2(num, number_list[i_num + 1]))
    if i_num == 8:
        break
print(result1)
print(number_list)

# зачёт!
