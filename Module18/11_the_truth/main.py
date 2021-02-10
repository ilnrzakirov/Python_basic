def ceasar_cipher(text, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 26] if sym not in sym_list else sym) for sym in text.lower()]
    new_text = ''
    for i_char in char_list:
        new_text += i_char
    return new_text


alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 26
shift = 25
sym_list = ".,/!?)(+ -"
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt ' \
       'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf ' \
       'dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt'

output_text = ceasar_cipher(text, shift)
print(output_text)

# как я понимаю тут не только сдвиг, но и перестановка в слове utifulbea = beautiful  с конца 3 буквы в начало
# beautiful is better than и к концу строки количество перенесенных букв увеличивается icitexpl = explicit -4
# esimpl = simple - 5  и "/" вероятно точка y/ugl = ugly. и  ex/compl = complex.

output_text1 = ""
for sym in output_text:
    if sym == "/":
        output_text1 += "."
    else:
        output_text1 += sym

# после каждой точки увеличивается количество перенесенных букв.
print(output_text1)


def transfer(word, quantity):  # функция перестановки букв
    if len(word) < quantity:
        quantity = quantity - len(word)
    new_word = word[-quantity:] + word[:-quantity]
    return new_word


output_text1 = output_text1.split()

quantity = 3
output_text2 = ""

for i_team in output_text1:
    remains = transfer(i_team, quantity)
    if i_team != "si":  # если реализовать перестановку от количества букв то is превратится в si и наоборот
        output_text2 += remains + " "
    else:
        output_text2 += "is" + " "
    if "." in i_team:
        quantity += 1
print(output_text2)

# Взял по большое текста, алгоритм снова не работает -( в конце перевод букв смешаны. 4/2/4 и 3/1/3 только
# не понятно как все это впихнуть в один цикл
# , действительно, вместо "tfla is etterb ntha nested. " должно получится
#  "flat is better than nested.", давайте подумаем ещё =) Вы близки к разгадке.
# Понял я где недоделал. Если количество передвигаемых букв больше слово, то передвигается только остаток от их разности
# =) Совершенно верно! =)
# зачёт!