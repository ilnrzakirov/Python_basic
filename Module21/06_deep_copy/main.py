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

def constructor (struct, n):
    if n == 0:
        return None
    name = input("Введите название продукта для нового сайта: ")
    site["html"]["head"]["title"] = "Куплю/продам {} недорого".format(name)
    site["html"]["body"]["h2"] = "У нас самая низкая цена на {}".format(name)
    return print(struct), constructor(struct, n -1)




n = int(input("Сколько сайтов: "))
constructor(site, n)

