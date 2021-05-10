

class Square:

    def __init__(self, number: int) -> None:
        self.stop_number = number
        self.cur_val = 1
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_val <= self.stop_number:
            self.result = self.cur_val ** 2
            self.cur_val += 1
            return self.result
        raise StopIteration

def square_gen(number: int):

    for num in range(number):
        yield num ** 2


square =(num ** 2 for num in range(5))
for num in square:
    print(num, end="\n")


square = Square(3)
for i_value in square:
    print(i_value)



