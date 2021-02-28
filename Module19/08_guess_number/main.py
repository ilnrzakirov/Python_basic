import random

max_number = int(input("Введите макисмальное число: "))

answer_boris = ""
answer_dict = dict()

number_artem = random.randint(0, max_number)
print(number_artem)
while answer_boris != "Помогите!":
    answer_boris = input("Нужное число есть среди вот этих чисел: ")
    if answer_boris == "Помогите!":
        break
    if str(number_artem) in answer_boris.split():
        answer_artem = "Да"
        print("Ответ Артема: Да")
    else:
        answer_artem = "Нет"
        print("Ответ Артема: Нет")
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

# , ответ Артёма у пользователя запрашивать не нужно.
#  "Да" или "Нет" должен вывести наш код после проверки =)
# зачёт!
