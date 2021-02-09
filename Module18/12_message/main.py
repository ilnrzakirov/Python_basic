text = input("Введите текст: ")
sym_list = ".,/!?)(+: "
new_text = ""
text1 = text.split()
new_word = ""


for i_word in text1:
    for i_team in i_word:
        if not i_team in sym_list:
            new_word = i_team + new_word
        else:
            new_word += i_team
    new_text += new_word + " "
    new_word = ""

print(new_text)