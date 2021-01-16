print("Введите координаты: ")
x = float(input("x: "))
y = float(input("y: "))
r = float(input("Введите радиус: "))
result = x ** 2 + y ** 2

if result <= r:
    print("Монетка где то рядом")
else:
    print("Монетки в области нет")

