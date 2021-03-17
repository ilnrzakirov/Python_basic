site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def constructor(struct, name):
    if "title" in struct.keys():
        struct["title"] = "Куплю/продам {} недорого".format(name)
    if "h2" in struct.keys():
        struct["h2"] = "У нас самая низкая цена на {}".format(name)
    for item in struct.values():
        if isinstance(item, dict):
            constructor(item, name)

def print_struct (struct):
    for item in struct.items():
        if isinstance(item, dict):
            print_struct(item)
        else:
            print(item)

n = int(input("Сколько сайтов: "))
for _ in range(n):
    name = input("Введите название продукта для нового сайта: ")
    constructor(site, name)
    print_struct(site)

# TODO, необходимо создать вывод структуры новых сайтов для пользователей.
#  Потребуется функция для
#  1. смены значений в тегах (ключах) title и h2.
#  При помощи цикла и рекурсии необходимо идти по словарю и проверять,
#  если есть необходимый тег в ключах словаря, меняем его значение,
#  если нет проверяем, является ли текущее значение словарём и проходим глубже при помощи рекурсии.
#  2. Для вывода структуры сайта на дисплей.
#  При помощи цикла и рекурсии необходимо идти по словарю и проверять, является ли следующее значение словарём.
#  Если да, реализуем рекурсию, если нет, выводим структуру при помощи print.
#  Если нет, проваливаемся глубже.
