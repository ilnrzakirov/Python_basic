class Wather:

    def __init__(self):
        self.name = "wather"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm
        elif isinstance(other, Fire):
            return Steam
        elif isinstance(other, Ground):
            return Dirt
        else:
            return None


class Ground:

    def __init__(self):
        self.name = "ground"

    def __add__(self, other):
        if isinstance(other, Wather):
            return Dirt
        elif isinstance(other, Air):
            return Dust
        elif isinstance(other, Fire):
            return Lava
        else:
            return None

class Fire:

    def __init__(self):
        self.name = "fire"

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning
        elif isinstance(other, Ground):
            return Lava
        elif isinstance(other, Wather):
            return Steam
        else:
            return None


class Air:

    def __init__(self):
        self.name = "air"

    def __add__(self, other):
        if isinstance(other, Wather):
            return Storm
        elif isinstance(other, Fire):
            return Lightning
        elif isinstance(other, Ground):
            return Dust
        else:
            return None

class Storm:
    name = "storm"

class Steam:
    name = "steam"

class Dirt:
    name = "dirt"

class Lightning:
    name = "lightning"

class Dust:
    name = "dust"

class Lava:
    name = "lava"


water = Wather()
ground = Ground()
fire = Fire()
air = Air()

other = water + ground
print(other)