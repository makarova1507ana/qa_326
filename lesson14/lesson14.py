# # ------------------- Функции ---------------------- #
# # фукнция - СОХРАНЕННЫЙ набор действий выполняющий какую-то конкретную задачу
# # def (define - объявлять) название_функции ()
# #    инструкции (ваш код)
#
# from turtle import*
# from time import sleep
#
#
# # def function_name(param_1, param_2, ... param_n)
# # param(параметр, аргумент) - переменная
#
# # рисование треугольника
# def draw_triangle(a: int, color_side: str): # a - сторона теругольника
#     try:
#         for i in range(3):
#                 color(color_side)
#                 forward(a)
#                 left(120)
#     except:
#         print('error types')
#
# # #--------------ПРИМЕР----------------#
# # draw_triangle(100, 'black') #int(input())
# # sleep(2)
# # draw_triangle('100', 'black') # НЕ выполнится потому что неверный тип данных
# # draw_triangle(color_side='red', a=50)
# # sleep(2)
# # draw_triangle(10, 'green')
# # sleep(5)
#
#
#
#
# # ------------------------Задача--------------------------#
# # создать функцию квадрата с параметром стороны
# # нарисовать при помощи этой функции нарисовать узор по картинке функция_квадрат.png
#
# from turtle import *
# def draw_square(a):# a -локальная
#     for i in range(4):
#         forward(a)
#         left(90)
#
# # for a in range(200, 100, -20):
# #     draw_square(a)# a -локальная
# #
# # exitonclick()
#
#
#
#
# # ------------------------Задача--------------------------#
#
# # ГЕНЕРАТОР
# # написать функцию для генерации email
# # Алгоритм
# # 1. подготовить символы для тетсирование "буквы цифры . @ спецсимволы"
# #   генериация валидных(псевдо) значений
# #    part1 = "буквы цифры" #набор из этих значений
# #    part2 = "@"
# #    part3 = "буквы цифры"
# #    part4 = "."
# #    part5 = "буквы"
# #
# #  email = part1+part2+part3+part4+part5
#
# # потенциальные параметры:
# # длина значений
# # валидный или невалидный
# # алфавит (набор символы)
# from random import choice
#
# #alpha - набор букв или букв и цифр и т.д.
# #len_str - кол -во в последовательности
# # результат функции -> строка
# def random_symbols(alpha: str, len_str: int):
#     part = ''
#     for count in range(len_str):
#         part += choice(alpha).lower()
#     return part
#
# # -----------ПРИМЕР работы функции random_symbols------------------#
# # alpha_latin = 'ABCDEFGHIKLMNOPQRSTVXYZ'
# # digit = '0123456789'
# # random_symbols(alpha_latin+digit, 3)
#
#
# def email_generator():
#     alpha_latin = 'ABCDEFGHIKLMNOPQRSTVXYZ'
#     alpha_kirill = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     digit = '0123456789'
#     exp_symbols = '&%$#^?,'
#     part1 = random_symbols(alpha_latin+digit, 10)
#     part2 = '@'
#     part3 = random_symbols(alpha_latin+digit, 4)
#     part4 = '.'
#     part5 = random_symbols(alpha_latin, 2)
#     email = part1 + part2 + part3 + part4 + part5
#     return email
#
# email = email_generator()
# print(email)
#
# # для ДЗ ------ генерация невалидных значений
#
#
#
# # Проверка по регулярному выражения валидности созданных email
# import re
#
# def is_valid_email(email: str):
#     tuple_ = re.match(r'\w{1,}@\w{1,}\.\w{1,}', email+'   *').span()
#     if tuple_[0] == 0 and tuple_[1] == len(email+'   &')-1:
#         return True
#     else:
#         return False
#
# print(is_valid_email(email))
#
#
#
#
#
#
# # ------ return - возвращаемое значение -----#
#
# # def sum_2_numbers(num1, num2):
# #     print(num1+num2)
# #
# # result = sum_2_numbers(5, 15)
# # print(result, type(result)) #у фукнции sum_2_numbers нет return
#
#
# # def sum_2_numbers(num1, num2):
# #     print(num1+num2)
# #     return num1+num2
# #
# # result = sum_2_numbers(5, 15)
# # print(result, type(result)) #потому что у функции есть return
#
# # length = len('fdfsf')





# # ------------------------Задача--------------------------#
# написать функцию(a, b, c), проверяет существование треугольника
# is_valid_triangle(a,b,c) -> bool

def is_valid_triangle(a:int , b:int, c:int):
    # if a+b > c and a+c > b and c+b > a:
    #     return True
    # return False

    #  можно сократить
    return a + b > c and a + c > b and c + b > a
#
# print(is_valid_triangle(5, 3, 4))




# # ------------------------Задача--------------------------#
# написать функцию(a, b, c), которая  возвращает площадь этого треугольника
# triangle_s(a,b,c) -> float
import random

def is_valid_triangle(a:int , b:int, c:int):
    return a + b > c and a + c > b and c + b > a
def area_of_triangle(a: int, b: int, c: int):
    #print(f'a = {a} , type(a)={type(a)}, b = {b} , type(b)={type(b)}, c = {c} , type(c)={type(c)}') #отладочная печать
    # - для дебаггер демоснрация кноки "step into" random.randint(0,1)
    if is_valid_triangle(a, b, c):
        p = ((a + b + c) / 2)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s
    return -1

print(f"s = {area_of_triangle(1,-1,1)}")

#--------------------- методы отладки-----------------------------#
# визуальный анализ (не требует запуска кода)
# отладочная печать (трубует запуска кода)
# deguber (трубует запуска кода и запуска отладчика)
# логи (трубует запуска кода (не трубует наличие человека))


#--------------- debuger ----------------------#
# debuger - отладчик специальная программа для пошагового выполнения кода




# # ------------------------Задача--------------------------#
# создать генератор даты
# требования к функции :
# функция должна принимать три целых числовых значения
# результат функции строка вида 00.00.0000 или 00/00/0000
# 01.01.2000
# 10/10/2000
def generate_date():
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(1000, 9999)
    sep = random.choice(['.', '/'])
    return f"{day}{sep}{month}{sep}{year}"

print(generate_date())
# создать функции проверки валидности даты
import re

def is_valid_date(date: str):
    l = re.findall(r'\d{1,2}[\./]\d{1,2}[\./]\d{4}', date)
    print(f'date = {date}  l ={l}')
    if l[0] == date:
        return True
    else:
        return False
print(is_valid_date(generate_date()))