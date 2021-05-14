from collections.abc import Iterable



def QHofstadter(qlist = list) -> Iterable [int]:
    qlist1 = qlist[:]
    n = 2
    while True:
        try:
            q = qlist1[n - qlist1[n -1]] + qlist1[n - qlist1[n -2]]
            qlist1.append(q)
            n += 1
            yield q
        except IndexError:
            return


qlist = [1, 1]
for item in QHofstadter(qlist):
    print(item)