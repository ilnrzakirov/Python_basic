str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
i_symbol = len(str1) - 1
chek = True

for symbol in str1:
    if not str2.count(symbol):
        print("Первую строку нельзя получить из второй со сдвигом")
        chek = False
        break
if chek == True:  # лучше просто "if chek"
    remains = str1[0]
    shift = str2.index(remains)
    for i_num in range(len(str1)):
        if str1[i_num] != str2[(i_num + shift) % len(str2)]:
            print("Первую строку нельзя получить из второй со сдвигом")
            chek = False
            break

if chek == True:  # лучше просто "if chek"
    print("Первая строка получается из второй со сдвигом {}".format(shift))

# зачёт!
