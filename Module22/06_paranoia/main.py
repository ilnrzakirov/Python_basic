import os


def chiper(text, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 26] if sym != "\n" else sym) for sym in text.lower()]
    new_text = ''
    for i_char in char_list:
        new_text += i_char
    return new_text


alphabet = 'abcdefghijklmnopqrstuvwxyz'
my_text_file = open("text.txt", 'r')
chipe_text = open("chiper_text.txt", "a")
shift = 0

for i_line in my_text_file:
    shift += 1
    string = chiper(i_line, shift)
    chipe_text.write(string)

my_text_file.close()
chipe_text.close()

# зачёт!
