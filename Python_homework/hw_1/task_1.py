number = input('Введите трёхзначное число: ')
sum = 0
for i in number:
    if i.isdigit():
        sum += int(i)
print(sum)



