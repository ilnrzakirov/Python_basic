def move (kernel1, kernel2, kernel3, n ):
    # , цикл лишний. Его у нас заменяет рекурсия.
    # TODO, пожалуйста, решите при помощи рекурсии. Возможно, вывзова функции внутри функции будет 2 =)
    for disk in kernel1:
        if disk == 1:
            kernel2.append(disk)
            kernel1.remove(1)



#n = int(input("Введите количество дисков: "))
n = 5
kernel1 = [number for number in range (n, 0, -1)]
kernel2 = []
kernel3 = []
move(kernel1, kernel2, kernel3, n)

print(kernel1)
print(kernel2)
print(kernel3)
