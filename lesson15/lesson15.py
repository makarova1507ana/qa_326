"""
Написать функцию для вычисления периметра
n-угольника(проверку на существование фигуры прописать
отдельную(ые) функцию(и)), применить эту функцию(и))
для вычисления периметра n-угольника
"""

# Алгоритм
# n -кол-во углов 3 и больше
# функция для проверки существует ли?

# сумма длин любых n−1
# сторон должна быть больше длины оставшейся стороны\

# a+b+c ...
# P_N_angle( [a,b,c,...])



# 1 example
# def P_N_angle(sides):
#     P = 0
#     for side in sides:
#         P += side
#     return P

def is_valid_polygon(sides):
    if len(sides) >= 3: # кол-во сторон
        list(sides).sort()
        if sum(sides[0:len(sides)-1]) > sides[-1]: # сумму самых маленьких > самой большой
            for side in sides:
                if side <= 0:# Есть ли отрицательные
                    return False
            return True
        return False
    return False
# сумма длин любых n−1
# сторон должна быть больше длины оставшейся стороны\
# 1, 2, 3
# 1+2 > 3
# 1+3 > 2
# 2+3 > 1


# sides = [1, 2, 3, 4]
# 1+2+3 > 25
# 1+2+4 > 3
# 1+3+4 > 2
# 2+3+4 > 1
# sides = [1, -2, 3, 4, 5, 6]
# sides.sort()
# print(sum(sides[0:len(sides)-1]) > 6 )







#P_N_angle(*sides) #*sides - кортеж
#P_N_angle()
#P_N_angle(1)
#P_N_angle(1,2,...)
def P_N_angle(*sides): # динамическое кол-во параметров
    # блок проверок
    if is_valid_polygon(sides):
        return sum(sides)
    return 0


#print(P_N_angle([1,2,3]))


# # динамическое кол-во именованных параметров
#
# def f(**values): # **values - словарь
#     print(values)
#
# f(v1=5,v2=4,v3=6)
#
# def f2(values: dict):
#     print(values)
# f2({"v1":5,"v2":4,"v3":6})



#—------------------------------- Задача —--------------------------------#
# # программа Тамагочи (питомец)
# # показатель настроения (0 до 100)
# # 0-20 - очень грустный
# # 21-40 - грустный
# # 41-60 - нейтральный
# # 61-80 - веселый
# # 81-99 -очень веселый
# # 100 - эйфория
# Напишите функцию.
# Она должна принимать именованные параметры “name” и “mood”.
# Показать настроение питомца.
def mood_Tamagochi(**Tamagochi): # Tamagochi{name: "Ivan", mood: 40}
    result = ""
    for key in Tamagochi:
        if type(Tamagochi[key]) == int:
            if 20 >= Tamagochi[key] > 0:
                result += " очень грустный"
        elif type(Tamagochi[key]) == str:
            result += Tamagochi[key]
    return result

# print(mood_Tamagochi(nickname="Ivan", mood=5))


def mood_Tamagochi(name: str = "no_name", mood: int = 50): # Tamagochi{name: "Ivan", mood: 40}
    if 20 >= mood > 0:
        return name + " очень грустный"



# print(mood_Tamagochi(name="Ivan", mood=5))
# print(mood_Tamagochi( mood=5))





# -------------------------функции высшего порядка и лямбда ---------------------------------- #
# лямбда функция
#

# def is_positive(num):
#     return num > 0


# lambda x: num > 0  # lambda == return
nums = [1, 2, 3, 4, 5]
is_positive = lambda num: num > 0 # is_positiv()


# for num in nums:
#     print(is_positive(num))


is_positive = 5
#print(is_positive)


def is_valid_triangle(a: int, b: int, c: int):
    return a + b > c and a + c > b and c + b > a #

def area_of_triangle(a: int, b: int, c: int):
    #print(f'a = {a} , type(a)={type(a)}, b = {b} , type(b)={type(b)}, c = {c} , type(c)={type(c)}') #отладочная печать
    # - для дебаггер демоснрация кноки "step into" random.randint(0,1)
    if (lambda a, b, c :  a + b > c and a + c > b and c + b > a)(a, b, c): # замена функции is_valid_triangle()
        p = ((a + b + c) / 2)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
    return -1

#print(f"s = {area_of_triangle(1,-1,1)}")



# функции высшего порядка - функции, которые в качетве аргумента принимают другую функцию
# filter

# Дан список целых чисел. Сформировать новый список, в которым все элементы
# будут четными

import functools


# nums = [1, 2, 3, 4, 56, 89, 44]

# nums = list(filter(lambda num: num % 2 == 0, nums))
# print(nums)


# Дан список целых чисел. Сформировать новый список, в которым все элементы
# # будут строковым типом
# nums = [1, 2, 3, 4, 56, 89, 44]
# nums = list(map(lambda num: str(num), nums))
# print(nums)

import re
# дан список строк. Создать список чисел
elements = ['1543', '2vcv', '3.5', '54,5', 'fgdfd', '89', '44', '-5454', '12--89']
reg_ex = r"-{0,}\d+\.{0,}\d{0,}[^A-z]"
nums = list(map(lambda element: element.replace(',', '.'), elements))
nums = list(filter(lambda element: re.fullmatch(reg_ex, element), nums))
nums = list(map(lambda num: float(num), nums))
print(nums)



# reduce()



