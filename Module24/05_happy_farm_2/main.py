class Potate:
    states = {0: "Отсутсвует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow (self):
        if self.state < 3:
            self.state += 1


    def print_state (self):
        print("Картошка {} сейчас {}".format( self.index, Potate.states[self.state]))

    def is_right(self):
        return self.state == 3  #  можно просто return self.state == 3.


class PotateGarden:

    def __init__(self, count):
        self.potates = [Potate(index) for index in  range (1, count + 1)]
        self.grooming = False

    def grow_all(self):
        if self.grooming:
            print("Картошка проростает")
            for i_potate in self.potates:
                i_potate.grow()

    def are_all_right(self):
        #  цикл получился лишний =)
            if not all(i_potate.is_right() for i_potate in self.potates):
                print("Кортошка еще не созрела")
                return False
            else:
                print("Вся кортошка созрела! Можно собирать")
                return True

class Gardener:

    def __init__(self, name, garden):
        self.name = name
        if isinstance(garden, PotateGarden):
            self.garden = garden
        self.harvest = []

    def grooming(self):
        #  предлагаю убрать параметр garden и обращаться сразу к своему саду.
            self.garden.grooming = True


    def harvest_crops(self):
        #  предлагаю убрать параметр garden и обращаться сразу к своему саду.
            if self.garden.are_all_right():
                self.harvest.append(self.garden.potates.copy())
                print('Собираем урожай')
            self.garden.potates.clear()

    def info(self):
        print("Садовник {} собрал {}".format(gardener.name, gardener.harvest))

my_garden = PotateGarden(5)
my_garden.are_all_right()
gardener = Gardener("Tom", my_garden)
gardener.grooming()
for _ in range (3):
    my_garden.grow_all()
    my_garden.are_all_right()
    if my_garden.are_all_right():
        gardener.harvest_crops()

gardener.info()

# , если картошка созрела, то на грядке её остаться не должно.
#  Пока что остаётся.
print(gardener.garden.potates)