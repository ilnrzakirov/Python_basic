import random

class Warrior:

    def __init__(self, name):
        self.warrior_name = name
        self.health = 100


unit_1 = Warrior("Unit1")
unit_2 = Warrior("Unit2")

while unit_1.health > 0 and unit_2.health > 0:
    remains = random.randint(1, 2)
    if remains == 1:
        unit_2.health -= 20
        print("Атаковал {}, у противника осталось {} очков жизни".format(unit_1.warrior_name, unit_2.health))
    if remains == 2:
        unit_1.health -= 20
        print("Атаковал {}, у противника осталось {} очков жизни".format(unit_2.warrior_name, unit_1.health))

if unit_1.health == 0:
    print("{} одержал победу".format(unit_2.warrior_name))
else:
    print("{} одержал победу".format(unit_1.warrior_name))