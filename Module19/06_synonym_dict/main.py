num_pairs = int(input("Введите количество пар слов: "))
pairs_dict = dict()
pairs_dict_rev = dict()

for i_pairs in range(1, num_pairs + 1):
    print("{} пара: ".format(i_pairs), end=" ")
    pair = input().lower().split(" - ")
    pairs_dict[pair[0]] = pair[1]
    pairs_dict_rev[pair[1]] = pair[0]

flag = False
while not flag:  # Правильнее просто "while not flag" =)
    word = input("Введите слово: ").lower()
    if word in pairs_dict:
        print("Синоним {}".format(pairs_dict[word]))
        flag = True
    elif word in pairs_dict_rev:
        print("Синоним {}".format(pairs_dict_rev[word]))
        flag = True
    else:
        print("Такого слова в словаре нет")

# зачёт!
