# ---------------------------Разбор задачи---------------------------------#

"""#  Задача 3
# Дано два числа .
# Найдите наибольшее четное число среди них.
# Если оно не существует, выведите фразу "not found"

a = int(input("Число 1"))
b = int(input("Число 2"))
if a > b:
    if a%2==0:
        print(a)
    elif b%2==0:
        print(b)
elif b > a:
    if a%2==0:
        print(a)
    elif b%2==0:
        print(b)
else:# a==b
  if a%2==0:
        print(a)
    else:
        print("not found")"""


#-------------------------2 способ  решения-----------------------------#
# #  Задача 3
# # Дано два числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"
#
# a = 6
# b = 7
# if a % 2 == 0 and b % 2 == 0:
#     if a > b:
#         print(a)
#     elif b > a:
#         print(b)
#     else:  # a==b
#         print(a)
# elif a % 2 == 0:
#     print(a)
# elif b % 2 == 0:
#     print(b)
# else:
#     print("not found")




# if elif - практике
# https://highload.today/python-if-else/
#-------------------------ЗАДАЧА-----------------------------#
#  Перевод Из мм в м и наоборот

choice_user = input("""
Выберите систему перевода
    1 - Из мм в м
    2 - Из м в мм """)
l = 100 #добавьте проверку на >=0

if choice_user == '1':
    print(f"{l} mm = {l/1000} m")
elif choice_user == '2':
    print(f"{l} m = {l * 1000} mm")
else:
    print("нет такой команды")






#-------------------------ЗАДАЧА-----------------------------#


# Дано:
# * кол-во товаров в коризине и их суммарная стоимость
# (один и тот же товар, цена соответсвена фикисрована на каждый товар)
# * кол-во товаров, которые нужно удалить из корзины
#
# Необходимо:
# показать сколько осталось товаров в коризне и итоговую стоимость

# Пример
# ВХОДНЫЕ ДАННЫЕ
# кол-во товаров в коризине  = 10
# суммарная стоимость = 1000
# кол-во товаров, которые нужно удалить из корзины =  3

# ВЫХОДНЫЕ ДАННЫЕ
# осталось товаров = 7
# итоговую стоимость = 700
#
#
# count_products = 10
# sum_products = 1000
# count_deleted_products = 3
#
# #  блок с указанием ошибок пользователя
# if count_products <= 0:
#     print("должен быть > 0")
# elif sum_products <= 0:
#     print("должен быть > 0")
# elif count_deleted_products < 0:
#     print("должен быть >=0")
#
# if count_products > 0 and sum_products > 0 and count_deleted_products >= 0:
#
#     if count_deleted_products <= count_products:
#         product_price = sum_products / count_products
#         result_count_product = count_products - count_deleted_products
#         result_sum_products = sum_products - (count_deleted_products * product_price)
#         print(f"В корзине осталось {result_count_product} товаров на сумму {result_sum_products} рублей")
#     else:
#         print(f"Нельзя удалить больше {count_products} продуктов")
# else:
#     print("Все значения должны быть больше 0")
#
#
#
#
#
#





