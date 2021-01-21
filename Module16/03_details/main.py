shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
result_1 = 0
result_2 = 0

name = input("Введите название: ")
for i_team in shop:
        for item in i_team:
                if item == name:
                        result_1 +=1
                        result_2 += i_team [1]

print(f"Количество деталей: {result_1}")
print(f"Общая стоимость: {result_2}")

