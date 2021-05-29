import math


class Square:
    def __init__(self, length: int):
        self.length = length

    def perimeter(self):
        p = 4 * self.length
        return p

    def square_area(self):
        s = self.length ** 2


class Triangle:
    def __init__(self, lenght: int, h: int):
        self.lenght = lenght
        self.h = h

    def perimeter(self):
        a = math.sqrt((1 * self.lenght ** 2) + self.h ** 2)
        p = self.lenght + a ** 2
        return p

    def square(self):
        s = 0.5 * self.lenght * self.h
        return s

# TODO, предлагаю для расчёта площади каждой фигуры использовать класс Mixin =)
