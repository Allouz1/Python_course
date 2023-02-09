
def get_and_chek_number_1():
    flag = True
    num_1 = int(input("Введите число 1: "))
    while flag:
        if num_1 >= 1000:
            print('number error!')
            num_1 = int(input("Введите число 1: "))
        else:
            flag = False
    return num_1

def get_and_chek_number_2():
    flag = True
    num_2 = int(input("Введите число 2: "))
    while flag:
        if num_2 >= 1000:
            print('number error!')
            num_2 = int(input("Введите число 2: "))
        else:
            flag = False
    return num_2

num_X = get_and_chek_number_1()
num_Y = get_and_chek_number_2()
s = (num_X - int((num_X**2 - 4 * num_Y)**0.5))//2
p = (num_X + int((num_X**2 - 4 * num_Y)**0.5))//2
print(s, p)