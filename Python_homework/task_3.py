number = input('Введите шестизначное число')
sum_1 = 0
sum_2 = 0

for i in range(len(number)):
    if i <= 2:
        sum_1 += int(number[i])
    else:
        sum_2 += int(number[i])

if sum_1 == sum_2:
    print('Ура! билет счастливый')
else:
    print('Блин, не повезло(')
