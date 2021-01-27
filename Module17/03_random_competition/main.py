import random

frst_squad = [round(random.uniform(5, 10), 2) for _ in range (20)]
scnd_squad = [round(random.uniform(5, 10), 2) for _ in range (20)]
vic_list = [(frst_squad[x] if frst_squad[x] >= scnd_squad[x] else scnd_squad[x] ) for x in range (20)]

print(f'Первая команда {frst_squad}')
print(f'Вторая команда {scnd_squad}')
print(f'Победители тура {vic_list}')