people = {
    "Сидоров Никита": 35,
    "Сидорова Алина": 34,
    "Сидоров Павел": 25,
    "Петров Павел": 40
}

surname = input("Введите фамилию: ").capitalize()
if surname.endswith("а"):
    surname = surname[:-2]

for i_key, i_value in people.items():
    if surname in i_key:
        print(i_key, i_value)

# зачёт!
