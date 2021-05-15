from collections.abc import Iterable
from typing import Type


# , возможно, возвращать лучше Type['QHofstadter'].
#  Предварительно импортировав Type из модуля typing.



# , предлагаю попробовать решить задание классов итератором и описать вычисления в методе __next__.
#  В таком случае, цикл while не потребуется. =)
class QHof:

    def __init__(self):
        self.Q = [1, 1]

    def __iter__(self):
        return self

    def __next__(self):
        q = self.Q[- self.Q[-1]] + self.Q[-self.Q[-2]]
        self.Q.append(q)
        return q

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


#qlist = [1, 1]
#for item in QHofstadter(qlist):
#    print(item)



