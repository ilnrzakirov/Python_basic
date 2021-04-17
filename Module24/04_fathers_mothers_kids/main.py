
class Parent:

    def __init__(self, name, age):
        self.name = name
        self.parent_age = age
        self.children = []

    def info (self):
        print("Имя: {}, возраст: {}, Список детей: {}".format(
            self.name, self.parent_age, self.children))

    def calm_child (self, object):
        if isinstance(object, Child):
            object.happy = True

    def feed_child (self, object):
        if isinstance(object, Child):
            object.hunger = False


class Child:

    def __init__(self, name, age):
        self.child_name = name
        self.child_age = age
        self.happy = True
        self.hunger = False
