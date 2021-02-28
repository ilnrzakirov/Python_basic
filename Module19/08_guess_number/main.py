max_number = int(input("Введите макисмальное число: "))

answer_boris = ""
answer_dict = dict()
while answer_boris != "Помогите!":
    answer_boris = input("Нужное число есть среди вот этих чисел: ")
    if answer_boris == "Помогите!":
        break
    answer_artem = input("Ответ Артема: ")
    if answer_artem == "Да":
        if "Да" in answer_dict:
            answer_dict["Да"].append(answer_boris.split())
        else:
            answer_dict["Да"] = answer_boris.split()
    elif answer_artem == "Нет":
        if "Нет" in answer_dict:
            answer_dict["Нет"].append(answer_boris.split())
        else:
            answer_dict["Нет"] = answer_boris.split()

for sym in answer_dict["Нет"]:
    if sym in answer_dict["Да"]:
        answer_dict["Да"].remove(sym)

print('Артем мог загадать числа: ', end="")
for sym in answer_dict["Да"]:
    print(sym, end=" ")

# TODO, ответ Артёма у пользователя запрашивать не нужно.
#  "Да" или "Нет" должен вывести наш код после проверки =)
