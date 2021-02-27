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

print("Лампа -", store[goods["Лампа"]][0]["quantity"], "шт, стоимость", store[goods["Лампа"]][0]["quantity"] *
      store[goods["Лампа"]][0]["price"], "руб.")
print("Стол - ", store[goods['Стол']][0]["quantity"] + store[goods['Стол']][1]["quantity"], "шт, стоимость",
      store[goods['Стол']][0]["quantity"] * store[goods['Стол']][0]["price"] + store[goods['Стол']][1]["quantity"] *
      store[goods['Стол']][1]["price"], "руб.")
print("Диван - ", store[goods['Диван']][0]["quantity"] + store[goods['Диван']][1]["quantity"], "шт, стоимость",
      store[goods['Диван']][0]["quantity"] * store[goods['Диван']][0]["price"] + store[goods['Диван']][1]["quantity"]*
      store[goods['Диван']][1]["price"], "руб.")
print("Стул - ", store[goods['Стул']][0]["quantity"] + store[goods['Стул']][1]["quantity"] + store[goods['Стул']][2]["quantity"],
      "штб стоимость", store[goods['Стул']][0]["quantity"] * store[goods['Стул']][0]["price"] + store[goods['Стул']][1]["quantity"] *
      store[goods['Стул']][1]["price"] + store[goods['Стул']][2]["quantity"] * store[goods['Стул']][2]["price"], "руб.")
