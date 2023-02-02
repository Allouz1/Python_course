# <- Типы данных. Интрополяция ->

# g = None # Пустое значени
# b = True # Bool

# n = 5 # Целые число
# s = 'fsd\'fsd' # Строка
# f = 4.34 # дробные числа
# print(s, n, f)
# print(f'{n} - {s} - {f}')
# print('{} - {} - {}'.format(n, f, s))

# <- Ввод данных. Замена пипов данных. ->

# print('Ввевите первую строку: ')
# a = int(input()) # Ввод данных
# b = int(input('Введите второ число: '))
# print(a, '+', b, '=', a + b)

# <- Округление ->

# a = 5.898923
# b = 4.53252
# print(round(a * b, 2))
# round(1.4123, 2) # 1 - число, 2 - колличество знаков после запятой

# <- Сокращённые операции присваивания ->

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# <- Сравнение в Python ->

# a = 1 > 4
# print(a) # False
# # —------------------------------------
# a = 1 < 4 and 5 > 2
# print(a) # True
# # —------------------------------------
# a = 1 == 2
# print(a) # False
# # —------------------------------------
# a = 1 != 2
# print(a) # True
# # —------------------------------------
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# # —------------------------------------
# a = 1 < 3 < 5 < 10
# print (a) # True

# <- Управляющие конструкции: if, if-else ->

# if condition:
#     operator 1
#     operator 2
#     ...
# else:
#     operator n + 1
#     operator n + 2
#     ...

# <- Условие elif ->

# if condition:
#     operator 1
# elif condition1:
#     operator n + 1
# elif condition2:
#     operator n * 2
# else:
#     operator

# <- Сложные условия ->

# if condition1 and condition2: # выполнится, когда оба условия окажутся верными
#     operator

# if condition3 or condition4: # выполнится, когда хотя бы одно из условий окажется верным
#     operator



a = 'qwerty'

for i in a:
    print(i)


