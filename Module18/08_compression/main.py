text = input("Введите строку: ")
symbol_str = ""
symbol = ""

# TODO, в первом цикле range и len лишние =)
#  Можно просто идти в цикле по строке.
for _ in range (len(text)):
    for number in range(len(text), 0, - 1):
        if number != 0:
            symbol = text[0] * number
        else:
            symbol = text[0]
        if text.startswith(symbol):
            symbol_str += text[0] + str(number)
            text = text [number : ]
            break

print(symbol_str)
