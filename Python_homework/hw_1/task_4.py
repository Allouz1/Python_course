n = int(input())
m = int(input())
k = int(input())

if n * m < k or k == n * m:
    print ('Нет')
elif k % m == 0 or k % n == 0:
    print ('Да')
else:
    print ('Нет')