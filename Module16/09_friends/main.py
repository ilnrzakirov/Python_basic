frends = int(input("Количество друзей: "))
voucher = int(input("Количество расписок: "))
sender = 0
recipient = 0
frends_bank = []

for num in range (1, frends + 1):
    frends_bank.append(list(range(num, num + 2)))
    frends_bank[num - 1][1] = 0


for number in range (voucher):
    print(f"{number + 1} расписка ")
    sender = int(input("От кого: "))
    recipient = int(input("Кому: "))
    summ = int(input("Cумма: "))
    frends_bank[sender - 1][1] -= summ
    frends_bank[recipient - 1][1] += summ

print("Баланс друзей")
for i_team in range (frends):
    print(f"{frends_bank[i_team][0]} : {frends_bank[i_team][1]}")