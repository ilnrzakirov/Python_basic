# TODO здесь писать код
l = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р',
        'с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
text = input("Введите сообщение: ")
shift = int(input("Сдвиг: "))
encrypted = ""

for symbol in text:
    if symbol != " ":
        i_symbol = l.index(symbol)
        if i_symbol + shift >= len(l):
            remains = len(l) - (i_symbol) + 1
            shift = remains - shift
            encrypted += l[i_symbol + abs(shift)]
            continue

        encrypted += l[i_symbol + shift]


print(encrypted)
