
def find_object (search_object, struct, level = 0, chek = 0):
    # TODO, возможно, выходить стоит если уровень строго меньше максимального
    if level < chek and level !=0:
        return None
    if search_object in struct:
        return struct[search_object]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            chek += 1
            result = find_object(search_object, sub_struct, level, chek)
            if result:
                break
    # TODO, есть вероятность, что код ниже лишний. Необходимо немного поправить первую часть функции.
    else:
        return  None

    return result

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


level = int(input("Введите уровень (если хотите искать на всех уровнях введите 0: "))
search_object = input("Что ищем: ")
value = find_object(search_object, site, level)
if value:
    print(value)
else:
    print("Такого ключа в структуре нет")

# TODO Введите уровень (если хотите искать на всех уровнях введите 0: 0
#  Что ищем: title
#  Такого ключа в структуре нет.
