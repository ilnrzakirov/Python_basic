import random


class Person:
    __total_eat = 0

    def __init__(self, name, satiety, happiness, house):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        self.alive = True
        # , если нет, то может сделать значение дома равным None? =)
        if isinstance(house, House):
            self.house = house
        else:
            self.house = None


    def eat(self):
        # , если нет еды, то не поели.
        if self.house.food > 30:
            self.satiety += 30
            self.house.food -= 30
            self.__total_eat += 30
        else:
            print("Недостаточно еды")

    def get_total_eat(self):
        return self.__total_eat

    def settle_cat(self, cat):
        if isinstance(cat, Cat):
            cat.house = self.house

    def act(self):
        if self.satiety <= 0:
            self.alive = False
            print("{} умер".format(self.name))


class Husband(Person):
    __total_money = 100


    def __init__(self, name, house, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness, house)
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        self.house = house

    def play(self):
        self.happiness += 20
        self.satiety -= 10


    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def work(self):
        self.house.mnoney += 150
        self.__total_money += 150
        self.satiety -= 10

    def get_total_money(self):
        return self.__total_money

    def  act(self):

        # TODO, Если человек умер, то действия в этом методе не должны происходить.
        #  Возможно, стоит добавить Метод act у Родительского класса с подобной проверкой.

        if self.satiety < 30:
            if house.food < 30:
                self.satiety -= 10
                self.work()
            else:
                self.eat()
                print("{} решил поесть".format(self.name))
        elif self.happiness < 20:
            number = random.randint (1, 2)
            if number == 1:
                self.play()
                print("{} играет в компьютерные игры".format(self.name))
            else:
                self.petting_cat()
                print("{} играет с котом". format(self.name))
        elif self.house.mnoney < 150:
            self.work()
            print("{} пошел на работу".format(self.name))
        else:
            self.work()

class Wife(Person):

    def __init__(self, name, house, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness, house)
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        self.house = house

    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def shopping(self):
        # , если денег нет, то не купила.
        if self.house.mnoney > 60:
            self.house.food += 60
            self.house.cats_food += 10
            self.house.mnoney -= 60
            self.satiety -= 10
        else:
            print("Недостаточно денег для покупки еды")

    def coat(self):
        # , если денег нет, то не купила.
        if self.house.mnoney > 350:
            self.happiness += 60
            self.house.coat += 1
            self.house.mnoney -= 350
            self.satiety -= 10
        else:
            print("Недостаточно денег для покупки шубы")

    def cleaning(self):
        self.house.dirt -= 100
        if self.house.dirt > 90:
            self.happiness -= 5
        self.satiety -= 10


    def act(self):
        if self.satiety < 30:
            if house.food < 30:
                self.satiety -= 10
                self.shopping()
            else:
                self.eat()
                print("{} решила поесть ".format(self.name))
        elif self.house.mnoney > 650:
            self.coat()
            print("{} решила купить шубу".format(self.name))
        elif self.house.dirt > 80:
            self.cleaning()
            print("{} решила убраться в квартире".format(self.name))
        else:
            self.petting_cat()

class Cat():

    # TODO, предлагаю добавить метод у человека "Поселить кота" и передавать коту "свой" дом в новом методе =)
    def __init__(self, name, satiety = 30):
        self.name = name
        self.satiety =satiety

    def eat(self):
        # , если еды нет, то не поел.
        if self.house.cats_food > 10:
            self.satiety += 20
            self.house.cats_food -= 10
        else:
            print("Недостаточно еды для кота")

    def sleep(self):
        self.satiety -= 10

    def hooliganism(self):
        self.satiety -= 10
        self.house.dirt += 10



    def act(self):
        if self.satiety < 20:
            self.eat()
            print("Кот ест")
            if self.house.cats_food < 10:
                self.satiety -= 10
        else:
            number = random.randint(1, 2)
            if number == 1:
                self.hooliganism()
                print("кот хулиганничает")
            else:
                self.sleep()
                print("Кот спит")

class House:

    def __init__(self):
        self.mnoney = 100
        self.food = 50
        self.cats_food = 30
        self.dirt = 0
        self.coat = 0




house = House()
cat = Cat("cat")
man = Husband("man", house)
man.settle_cat(cat)
woman = Wife("woman", house)
for day in range(365):
    man.act()
    cat.act()
    woman.act()
print("Всего куплено шуб {}, сьедино {} еды, заработано денег: {}".format(house.coat,
            man.get_total_eat() + woman.get_total_eat(), man.get_total_money() ))