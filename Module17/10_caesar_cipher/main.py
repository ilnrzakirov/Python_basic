# TODO здесь писать код
l = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р',
        'с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
text = input("Введите сообщение: ")
shift = int(input("Сдвиг: "))
encrypted = ""
remains = 0

for symbol in text:
    if symbol !=" ":
        i_team = l.index(symbol)
        if i_team + shift > 31:
            shift1 = shift - (31 - i_team)
            encrypted += l[shift1 - 1]
            continue
        encrypted += l[i_team + shift]
    else:
        encrypted += symbol

print(encrypted)
