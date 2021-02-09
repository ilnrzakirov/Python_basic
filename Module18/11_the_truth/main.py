def ceasar_cipher (text, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 26] if sym not in sym_list else sym) for sym in text.lower()]
    new_text = ''
    for i_char in char_list:
        new_text += i_char
    return new_text

alphabet = 'abcdefghijklmnopqrstuvwxyz' #26
shift = 25
sym_list = ".,/!?)(+ "
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm'


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

print(output_text1)
