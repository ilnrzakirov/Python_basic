from collections.abc import Iterable
from typing import Type


# , возможно, возвращать лучше Type['QHofstadter'].
#  Предварительно импортировав Type из модуля typing.


# , предлагаю попробовать решить задание классов итератором и описать вычисления в методе __next__.
#  В таком случае, цикл while не потребуется. =)
class QHof:

    def __init__(self):
        self.Q = [1, 1]
        self.count = 0

    def __iter__(self):
        # , стоит добавить переменную счётчик равную "0"
        #  Далее в next первый элемент будет равен "переменная счётчик" + 1 - предыдущее значение
        #  второй элемент будет равен "переменная счётчик" + 1 - ПРЕДпредыдущее значение
        return self

    def __next__(self):
        q1 = self.count + 1 - self.Q[-1]
        q2 = self.count + 1 - self.Q[-2]
#        q = self.Q[- self.Q[-1]] + self.Q[-self.Q[-2]]
        # , по идее, за 1 раз необходимо создавать 2 числа и 2 числа добавлять в список.
        self.Q.append(q1)
        self.Q.append(q2)

        return self.Q


def QHofstadter(qlist=list) -> Type["QHofstadter"]:
    # , сисок в решении лишний.
    #  Генератор не должен хранить в себе массивы с данными =)
    n = 2
    while True:
        # , блок try/except лишний.
        q = qlist[n - qlist[n - 1]] + qlist[n - qlist[n - 2]]
        qlist.append(q)
        n += 1
        yield q

# qlist = [1, 1]
# for item in QHofstadter(qlist):
#    print(item)
