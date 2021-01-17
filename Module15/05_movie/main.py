films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
answer =""
my_films = []

while answer != "end":
    answer = input("Введите название фильма: ")
    if answer in films:
        my_films.append(answer)
    elif answer == "end":
        break
    elif answer not in films:
        print("Этого фильма в списке рецензий нет ")
print(f'Список любимых фильмов с рецензией {my_films}')

# зачёт!