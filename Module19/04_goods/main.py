goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# , Ильнур, ответ верный, давайте поработаем над стилем.
#  Предлагаю для store[goods['Стол']] и т.д. придумать переменные и использовать их в вычислениях,
#  в таком случае, кода станет меньше. И пропадёт большое кол-во [[[]]].
table = store[goods['Стол']]
lamp = store[goods["Лампа"]]
sofa = store[goods['Диван']]
chair = store[goods['Стул']]
lamp_total_price = lamp[0]["quantity"] * lamp[0]["price"]
# TODO, в коде есть небольшая опечатка, в связи с этим, итоговая сумма столов пока что выводится некорректно.
table_total_quantity = table[0]["quantity"] + table[1]["quantity"]
table_total_price = table[0]["quantity"] * table[0]["price"]
sofa_total_quantity = sofa[0]["quantity"] + sofa[1]["quantity"]
sofa_total_price = sofa[0]["quantity"] * sofa[0]["price"] + sofa[1]["quantity"] * sofa[1]["price"]
chair_total_quantity = chair[0]["quantity"] + chair[1]["quantity"] + chair[2]["quantity"]
# Пожалуйста, обратите внимание на перенос строки при больших вычислениях.
chair_total_price = (
        chair[0]["quantity"] * chair[0]["price"]
        + chair[1]["quantity"] * chair[1]["price"]
        + chair[2]["quantity"] * chair[2]["price"]
)

# , Делать большое количество вычислений в print не очень хорошо.
#  Предлагаю создать дополнительные переменные для вычислений и уже их вывести при помощи print.

print("Лампа -", lamp[0]["quantity"], "шт, стоимость", lamp_total_price, "руб.")
print("Стол - ", table_total_quantity, "шт, стоимость", table_total_price, "руб.")
print("Диван - ", sofa_total_quantity, "шт, стоимость", sofa_total_price, "руб.")
print("Стул - ", chair_total_quantity,
      "штб стоимость", chair_total_price, "руб.")


