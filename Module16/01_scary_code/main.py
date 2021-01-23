first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]

first_list.extend(second_list)
count_list = first_list.count(5)
print(f"Количество цифр 5 при первом объединении: {count_list}")

# наверное было бы правильно сохранить результат вычисления first_list.count(5)
# и использовать его в выводе и в range.
for _ in range(count_list):
    first_list.remove(5)
first_list.extend(third_list)
print(f"Количество цифр 3 при втором объединении: {first_list.count(3)}")

print(first_list)

# зачёт!
# зачёт!
