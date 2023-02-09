n = int(input('Введите число: '))
lst = [1]
temp = 1

while temp * 2 < n:
    temp *= 2
    lst.append(temp)
print(lst)
