import collections


def can_be_poly(string: str) -> bool:
    res = list(filter(lambda count: count % 2 != 0 , collections.Counter(string).values()))
    if len(res) > 1:
        return False
    else:
        return True
#    one_letter = 0
#    for sym in sym_list:
#        if sym_list[sym] % 2 == 0:
#            continue
#        else:
#            one_letter += 1
#    if one_letter == 1 or one_letter == 0:
#        return True
#    else:
#        return False


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

# TODO, предлагаю попробовать добавить в решение функции filter и lambda и попробовать решить задание
#  без цикла for с условным оператором. =)
#  По идее, строка с вычислениями получится всего одна.
