def move(kernel1, kernel2, kernel3, n):
    if n == 1:
        print("Переложить диск 1 со стержня {} на стержень {}".format(kernel1, kernel3))
        return None
    move(kernel1, kernel3, kernel2, n - 1)
    print("Переложить диск {} со стержня {} на стержень {}".format(n, kernel1, kernel3))
    move(kernel2, kernel1, kernel3, n - 1)


#  цикл лишний. Его у нас заменяет рекурсия.
# , пожалуйста, решите при помощи рекурсии. Возможно, вывзова функции внутри функции будет 2 =)


n = int(input("Введите количество дисков: "))
kernel1, kernel2, kernel3, = "№1", "№2", "№3"
move(kernel1, kernel2, kernel3, n)

# зачёт!
