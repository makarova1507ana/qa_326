# # ----------------- Задание -----------------  # 
# """
# Напишите программу, которая будет считать полную
# стоимость всех товаров или со скидкой.
# Пользователь определяет кол-во товаров и цену за одну штуку
# """
#
# # 1 получить от пользователя кол-во товаров и цену за одну штуку
# count, cost, sale = int(input("count of items: ")), int(input("your cost: ")), int(input("your sale: "))
#
# # 2 предоставить пользователю выбор :
# #   * сумма товаров без учета скидки
# #   * сумма товаров с учетом скидки
# is_sale = input("Хотите ли посчитать сумма товаров со скидкой?")
# if is_sale == "да":
#     print(f" ваша сумма товаров со скидкой: {count*cost*(1+sale/100)}")
# if is_sale == "нет":
#     print(f" ваша сумма товаров  без скидки: {count*cost}")


#
# # ----------------- Задание -----------------  #
# """
# Напишите программу.
# Пользователь выбирает фигуру (квадрат или треугольник),
# черепеха рисует выбранную фигуру
# """
#
# from turtle import*
# from time import *
# figure = input('Выберете фигуру, квадрат или треугольник ').lower()# lower() -если написали с большой, переведет  в нижний регситр
# if figure == 'квадрат':
#     forward(120)
#     right(90)
#     forward(120)
#     right(90)
#     forward(120)
#     right(90)
#     forward(120)
#     right(90)
#     sleep(5)
#
# if figure == 'треугольник':
#     forward(120)
#     right(120)
#     forward(120)
#     right(120)
#     forward(120)
#     right(120)
#     sleep(5)
#
# # else:
# #     print('Надо выбрать только квадрат или треугольник')





# ЛОГИЧЕСКИЙ ТИП ДАННЫХ bool -> boolean
# True - правда (1)  False - ложь (0)
# числа преобразуется к логическому типу
# 0 - всегда ложь, все остальное правда
# '' - пустая строка это тоже ложь,все остальное правда

# проверить кратно ли число 3
# num = 33
# if num % 3: #  преобразование к логическому типу данных (0-> False)
#     print(f"{num} делится на 3")
# print(bool(0))
# print(bool(2.3))


# # РАБОЧИЙ ВАРИАНТ
# num = 33
# if num % 3 == 0: #  преобразование к логическому типу данных (0-> False)
#     print(f"{num} делится на 3")





#---------------------Вопросы знатокам----------------------------------#

# print(bool(True == 1))# True ->  1 ,   1 -> True
# # print(int(True))
# # print(bool(1))
# print(bool(True == 21))# False -> потому что разные типы данных
# print(bool(True == bool(21)))# True

# print(bool('1' == 1))
# print(type(int('1')))
# print(type(str(1)))





# -------------------логические операторы----------------------#
# and -
# or
