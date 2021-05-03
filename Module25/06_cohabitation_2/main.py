

class Person:

    def __init__(self, name, satiety, happiness, house):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        if isinstance(house, House):
            self.house = house

    def eat(self):
        self.satiety += 30
        self.house.food -= 30



class Husband(Person):

    def __init__(self, name, house, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness, house)
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        self.house = house

    def play(self):
        self.happiness += 20


    def petting_cat(self):
        self.happiness += 5

class Wife(Person):

    def __init__(self, name, house, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness, house)
        self.name = name
        self.satiety = satiety
        self.happiness = happiness
        self.house = house

    def petting_cat(self):
        self.happiness += 5

    def shopping(self):
        self.house.food += 10
        self.house.cats_food += 10
        self.house.mnoney -= 20

    def coat(self):
        self.happiness += 60
        self.house.coat += 1
        self.house.mnoney -= 350

    def cleaning(self):
        self.house.dirt -= 100
        if self.house.dirt > 90:
            self.happiness -= 5

class Cat():

    def __init__(self, name, house, satiety = 30):
        self.name = name
        self.satiety =satiety
        if isinstance(house, House):
            self.house = house

    def eat(self):
        self.satiety += 20
        self.house.cats_food -= 10

class House:

    def __init__(self, cat):
        self.mnoney = 100
        self.food = 50
        self.cats_food = 30
        self.dirt = 0
        if isinstance(cat, Cat):
            self.cat = cat
        self.coat = 0
