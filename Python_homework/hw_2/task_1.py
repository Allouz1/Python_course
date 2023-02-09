from random import randint

coin = int(input("Колличество монет: "))
lst_coin = []
count = 0

for c in range(coin):
    lst_coin.append(randint(0, 1))

print(lst_coin)

for temp in lst_coin:
    if temp == 0:
        count += 1
print(count)