
class MyDict:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        print(self.key, ":", self.value)


    def get(self, key):
        if key == self.key:
            return self.value
        else:
            return 0


num = MyDict("non", 212)
print(num.get("n2n"))