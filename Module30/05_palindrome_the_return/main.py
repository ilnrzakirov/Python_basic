import collections

def can_be_poly(string: str) -> bool:
    sym_list = collections.Counter(string)
    one_letter = 0
    for sym in sym_list:
        if sym_list[sym] % 2 == 0:
            continue
        else:
            one_letter += 1
    if one_letter == 1 or one_letter == 0:
        return True
    else:
        return False


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))