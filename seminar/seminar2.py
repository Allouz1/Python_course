from random import randint

# x = randint(0, 100)
#  if x > 50:
#      y = True
#  else:
#     y = False
#
# # y = True if x > 50 else False
# print(f'сгенерированно число {x}')
# print(y)
# i = 0
# sum = 0

# while i <= x:
#     sum += i
#     i += 1
#
# print(sum)

# sum_2 = 0
# for i in range(x + 1):
#     sum_2 += i
# print(sum_2)

# sp = ["fwgwe", 88, 55, True]
# for k,v in enumerate(sp):
#     print(k,v)

'''
По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

Input: 5

Output: 120
'''

# n = int(input('Введите число: '))
# i = 1
# result = 1
# while i <= n:
#     result *= i
#     i += 1
# print(result)

'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input: 5

Output: 6
'''

# num = int(input(': '))
# first = 0
# second = 1
# counter = 2
# while second <= num:
#     if second == num:
#         print(counter)
#         break
#     first, second = second, first + second
#     counter+=1
# else:
#     print(-1)


'''
Уставшие от необычно теплой зимы, 
жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10
Output: 2
'''
# from random import randint
#
# all_dyes = int(input('Введите число: '))   # Общее количество дней
# lst = []
# count = count_1 = 0
# count_1 = 0
#
# for i in range(all_dyes):
#     day = randint(-50, 50)
#     lst.append(day)
# print(lst)
#
# for j in lst:
#     if j >= 0:
#         count += 1
#         if count_1 < count:
#             count_1 = count
#     else:
#         count = 0
# print(count_1)

'''
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
'''
# N = int(input(': '))
# sp = []
# for i in range(N):
#     sp.append(int(input()))
#     min = sp[0]
#     max = sp[0]
# for i in range(N):
#     if sp[i] > max:
#     max = sp[i]
#     if sp[i] < min:
#     min = sp[i]
# print(min, max)







