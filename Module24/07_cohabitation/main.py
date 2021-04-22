import random


class People:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        if isinstance(house, House):
            self.house = house
        self.alive = True

    def eats(self):
        if self.house.food >= 20:
            self.satiety += 20
            self.house.food -= 20
            print("{} решил подкрепиться".format(self.name))
        else:
            print("Недостаточно еды в холодильнике, надо поработать")

    def work(self):
        if self.satiety >= 20:
            self.satiety -= 20
            self.house.money += 20
            print("{} немного поработал".format(self.name))
        elif self.satiety == 0:
            self.alive = False
        else:
            print("Нужно поесть")

    def play(self):
        if self.satiety >= 20:
            self.satiety -= 20
            print("{} решил поиграть".format(self.name))
        elif self.satiety == 0:
            self.alive = False
        else:
            print("Нужно поесть")

    def shop(self):
        if self.house.money >= 20:
            self.house.food += 20
            print("{} сходил за едой".format(self.name))
        else:
            print("Недостаточно денег для покупок")

    def act(self):
        number = random.randint(1, 6)
        if self.alive:
        # , если умер, действия не выполняются.
            if self.satiety < 20:
                self.eats()
            elif self.house.food < 20:
                self.shop()
            elif self.house.money < 50:
                self.work()
            elif number == 1:
                self.work()
            elif number == 2:
                self.eats()
            elif number > 2:
                self.play()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0


house = House()
Tom = People("Tom", house)
Vany = People("Vany", house)

#  предлагаю создать у человека метод act и перенести условный оператор в него.
#  В цикле запускать только метод act человека.
#  Если человек умер, из цикла стоит выйти.

for day in range(365):
    Tom.act()
    Vany.act()
    if Tom.alive == False:
        print("{} умер".format(Tom))
        break
    elif Vany.alive == False:
        print("{} умер".format(Vany))
        break
