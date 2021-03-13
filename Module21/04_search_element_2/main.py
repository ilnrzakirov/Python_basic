
def find_object (search_object, struct, level = 0, chek = 0):
    # TODO, возможно, выходить стоит если уровень строго меньше максимального
    if level == chek:
        return None
    if level == 0:  # TODO, возможно лишняя проверка
        if search_object in struct:
            return struct[search_object]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_object(search_object, sub_struct, level=0)
            if result:
                break
    # TODO, есть вероятность, что код ниже лишний. Необходимо немного поправить первую часть функции.
    else:
        result = None
    if level != 0 :
        chek += 1
        if search_object in struct:
            return struct[search_object]
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_object(search_object, sub_struct, level)
                if result:
                    break
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
