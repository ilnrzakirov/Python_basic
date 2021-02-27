def histogram (text):
    sym_dict = dict()
    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input("Введите текст: ").lower()
hist = histogram(text)

print("Оригинальный словарь частот: ")
for i_sym in sorted(hist.keys()):
    print(i_sym, ":", hist[i_sym])

hist_val = hist.values()
hist_key = hist.keys()


new_hist = dict()
count = 0
for i_key in hist_key:
    if hist[i_key] in new_hist:
        new_hist[hist[i_key]].append(i_key)
    else:
        new_hist[hist[i_key]] = []
        new_hist[hist[i_key]].append(i_key)

print("Инвертированный словарь частот: ")
for i_sym in sorted(new_hist.keys()):
    print(i_sym, ":", new_hist[i_sym])