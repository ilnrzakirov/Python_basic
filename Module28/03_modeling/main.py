import math
from typing import Any


class Square:
    def __init__(self, length: float):
        self._length = length

    def perimeter(self) -> float:
        p = 4 * self._length
        return p

    def square(self) -> float:
        s = self._length ** 2
        return s

    @property
    def length(self) -> float:
        return self._length  # TODO, таким образом возвращаем метод. Аргумент класса имеет немного другое название.

    @length.setter
    def length(self, length: float) -> None:
        self._length = length  # TODO, таким образом переопределяем метод, предлагаю добавить "_" к названию после self. =)


class FigureSquareMixin:
    @classmethod
    def square_figure(cls, figure_list: list) -> float:
        s = 0
        for figure in figure_list:
            s += figure.square()
        return s


class Triangle:
    def __init__(self, length: float, h: float):
        self._length = length
        self.h = h

    def perimeter(self) -> float:
        a = math.sqrt((1 * self._length ** 2) + self.h ** 2)
        p = self._length + a ** 2
        return p

    def square(self) -> float:
        s = 0.5 * self._length * self.h
        return s

    #  таким образом и метод класса и аргумент имеют одинаковое название => length.
    #  Стоит добавить к названию аргумента "_" =)
    @property
    def length(self):
        return self._length  # , таким образом возвращаем метод. Аргумент класса имеет немного другое название.

    @length.setter
    def length(self, length) -> None:
        self._length = length  # , таким образом переопределяем метод, предлагаю добавить "_" к названию после self. =)


class Pyramid(Triangle, Square, FigureSquareMixin):
    # , предлагаю для расчёта площади каждой фигуры использовать класс Mixin =)
    def __init__(self, length: float, h: float):
        super().__init__(length, h)
        self.element_pyramid: Any = [Triangle(length, h) for _ in range(4)]
        self.element_pyramid.append(Square(length))


class Cube(Square, FigureSquareMixin):
    def __init__(self, length: float):
        super().__init__(length)
        self.element_cube = [Square(length) for _ in range(6)]


p = Pyramid(5, 5)
print(p.square_figure(p.element_pyramid))
c = Cube(5)
print(c.square_figure(c.element_cube))

# зачёт!
