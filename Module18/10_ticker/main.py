str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
i_symbol = len(str1) -1
chek = True

for symbol in str1:
    if not str2.count(symbol):
        print("Первую строку нельзя получить из второй со сдвигом")
        chek = False
        break
if chek == True:
    remains = str1[0]
    remains = str2.index(remains)
    for i_team in str1:
        if

print(i_symbol_str1)