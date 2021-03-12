def fibonachi (num_pos, chek = 2, start = 0, res = 1):
    if num_pos == 1:
        return 1
    if chek == num_pos:
        return res + start
    chek +=1
    result = res + start
    start = res
    return fibonachi(num_pos, chek, start, result)

num_pos = int(input("Введите номер позиции: "))

print(fibonachi(num_pos))

