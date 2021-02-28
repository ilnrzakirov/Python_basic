string = input("Введите строку: ")

nok = 0
ok = 0
remains = 1
for sym in string:
    if sym not in string [remains:]:
        nok +=1
    else:
        ok += 1
    remains += 1

if nok - ok > 1:
    print("Нельзя сделать палиндром")
else:
    print('Можно сделать палиндром')