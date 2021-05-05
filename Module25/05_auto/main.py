import math


class Car:

    def __init__(self, name, x, y, degree):
        self.name = name
        self.x = x
        self.y = y
        self.degree = degree

    def move(self, distance):
        deltax = distance * math.cos(self.degree)
        deltay = distance * math.sin(self.degree)
        x2 = self.x + deltax
        y2 = self.y + deltay
        self.x = x2
        self.y = y2

    def rotation(self, degree):
        self.degree = degree

    def info(self):
        print("Автомобиль находтся x = {}, y = {}".format(self.x, self.y))


class Bus(Car):
    fare = 100
    bank = 0
    k = 1

    def __init__(self, name, x, y, degree):
        super().__init__(name, x, y, degree)
        self.passengers = 0

    def enter(self, passengers):
        self.passengers += passengers
        self.bank = self.fare * self.passengers * self.k

    def go_out(self, passengers):
        self.passengers -= passengers

    def move(self, distance):
        deltax = distance * math.cos(self.degree)
        deltay = distance * math.sin(self.degree)
        x2 = self.x + deltax
        y2 = self.y + deltay
        self.x = x2
        self.y = y2
        self.k += distance / 10

    # , Наконец, метод move должен быть переопределён, чтобы увеличивать количество денег
    #  в соответствии с количеством пассажиров и проезжающим расстоянием.
    # , к примеру, за каждый км, который проехал человек мы можем добавлять по 0.1 к коэффициенту стоимости проезда =)
