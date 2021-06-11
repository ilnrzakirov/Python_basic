import timeit


res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)

res2: float = timeit.timeit('"-".join([str(n) for n in range (100)])', number=10000)
print(res2)

res3: float = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(res3)