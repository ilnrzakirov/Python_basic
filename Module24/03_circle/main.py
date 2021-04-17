import math

class Circle:

    def __init__(self, x = 0, y = 0, r = 1):
        self.x = x
        self.y = y
        self.radius = r

    def square (self):
        s = math.pi * self.radius ** 2
        return s

    def perimeter (self):
        p = 2 * math.pi * self.radius
        return p

    def zoom (self, k):
        self.radius = self.radius * k

    def checking_intersection (self, object):
        if isinstance(object, Circle):
            suum_radius = self.radius + object.radius
            difference = self.radius - object.radius
            distans = math.sqrt((self.x - object.x) ** 2 + (self.y - object.y) ** 2)
            if difference < distans < suum_radius:
                return True
            else:
                return False

circle1 = Circle(0, 0, 1)
circle2 = Circle(1, 1, 2)
print(circle1.checking_intersection(circle2))