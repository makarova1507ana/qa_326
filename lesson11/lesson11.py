# # """задача
# # дан  список
# # запрещено использовать sort, max, count, sum, map
# # сформировать новый список, с положительными числами"""
# # from random import randint
# # nums = []
# # n = 10
# # for i in range(n):
# #     nums.append(randint(-100, 100))
# # new_nums = []
# # for num in nums: #!!!!!!!!!!   index - лучше num
# #     if num > 0:
# #         new_nums.append(num)
# # print(nums)
# # print(new_nums)
#
#
# # ----------------задача---------------------
# # Найдите количество различных элементов данного массива.
#
# numbers = [2,3,2,2,6,8,9,10]
#
# unique_numbers = set(numbers)
# print(unique_numbers)
# print(len(unique_numbers))

# #-------------------------------------Практика------------------------------------------------#
#
# # пользователь вводит пин-кодов (4 цифры)
# # необходимо проверить есть ли такой пин
# # в нашей базе пин-кодов
#
# # ввод
# # 1111, 2222, 3333 | 1111, 2222, 3333   |1111, 2222, 3333 | нет списка | 1111, 2222, 3333
# # 1111             | '1111'             |1122              | 1111      |нет пин-кода
#
# # вывод
# # Доступ разрешен  |Доступ разрешен    | Доступ запрещен |  Доступ запрещен | Доступ запрещен
# pin_codes = [1111, 2222, 3333]
# users_pin = '1111,0'
# try:
#     if int(users_pin) in pin_codes:
#         print("Доступ разрешен")
#     else:
#         print("Доступ запрещен")
# except:
#     print(" что-то пошло не так")


# # #-------------------------------------Задача------------------------------------------------#
# # Даны два списка чисел.
# # Посчитайте, сколько чисел содержится одновременно как
# # в первом списке, так и во втором.
# #
# # 1 3 2
# # 4 3 2
# #
# # 2
#
#
#
# # 1 1 2
# # 4 1 1
# #
# # 1
#
#
# # алгоритм
# # s1 = [1, 3, 2]
# # s2 = [4, 3, 2]
# # для каждого элемента списка s1:
# #       Если элемента списка s1 есть в списке s2:
# #            увеличаем значение счетчика
# s1 = []
# s2 = []
# counter = 0
# for el in set(s1):
#     if el in set(s2):
#         counter += 1
# print(counter)
# print(type(s1))




# #  -------------------- словарь ------------------------------ #
# #      * dictionary - словарь - ассоциативный массив
# # ключ(ДОЛЖЕН быть уникальным): значение
# dictionary = {"one": 1, "two": 2} # ключ: значение
#
# # print(dictionary["two"]) #обращение к элементу по ключу
#
# print(dictionary)
# dictionary["one"] = "один"
# print(dictionary)
# dictionary["three"] = 3
# print(dictionary)
# # print(dictionary['fffff']) # KeyError: 'fffff' нет такого ключа
#
# dictionary.pop("one")
# print(dictionary)


# dictionary = {"one": 1, "two": 2} # ключ: значение
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())

# # найти пары ключей и значений для введеного пользователя значений
#
# d = {"one": 2, "three": 3, "two": 2}
# num = 2
# for key in d:
#     if d[key] == num:
#         print(f"d[{key}] = {d[key]}")


#-------------------------------------Задача------------------------------------------------#
#пользователь вводит номер месяца, необходимо
# отобразить кол-во дней (нельзя использовать
# сторонние модули)

# 12
# 31

# months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# num_month = -1
# try:
#     print(f"в месяце номер {num_month} содержится  {months_days[num_month]} кол-во дней")
# except:
#     print("Неверное значение для месяца")

#-------------------------------------Задача------------------------------------------------#
#пользователь вводит кол-во дней, необходимо
# отобразить номера месяцев нельзя использовать
# сторонние модули)



# numbers_months = {28: [2], 29: [2], 30: [4, 6, 9, 11], 31: [1, 3, 5, 7, 8, 10, 12]}
# days = 31
# try:
#     for number_month in numbers_months[days]:
#         print(number_month)
# except:
#     print("неверно указно кл-во дней")




# # такая же задача, но дан другой словарь
# months_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# days = 31
# try:
#     for number in months_days:
#         if months_days[number] == days:
#             print(number)
# except:
#     print("неверно указно кл-во дней")




# #-------------------------------------Задача------------------------------------------------#
# # Вам дан словарь, состоящий из пар слов.
# # Каждое слово является синонимом к парному ему слову.
# # Все слова в словаре различны.
#
#
# # Отличный
# # Хороший
#
# # Хороший
# # Отличный
#
# # Добрый
# # нет синонимов
#
# word = input("Введите слово ")
# synonym = {'добрый': 'добродушный', 'красивый':'симпатичный', 'милый':'ласковый'}
#
# try:
#
#     for i in synonym:
#         if i == word:
#             print(f"Синомним слова {word} это {synonym[i]}")
#         elif synonym[i] == word:
#             print(f"Синомним слова {word} это {i}")
#
# except:
#     print("что-то пошло не так")
# finally:
#     print("Такого слова нет в словаре")



# # ------------------------------------Задача------------------------------#
# # Дан список чисел, необходимо посчитать кол-во каждого уникального числа
# # и сформировать из этих данных словарь
# #
# # ввод
# # 1 2 1 22
# #
# # вывод
# # число 1 встречается 2 раза
# # число 2 встречается 1 раз
# # число 22 встречается 1 раз
#
# # Алгоритм
# # выделить только уникальные значения (set())
# # сформировать словарь из уникальных чисел и их кол-во вхождений в списке
#
#
# l = [1, 2, 1, 22]
# unique_nums = set(l)
# d = {}
# for num in unique_nums:
#     #print(f"{num} встречается {l.count(num)}")
#     d[num] = l.count(num)
#
# for num in d:
#     print(f"{num} встречается {d[num]} раз")
#
# # # если пользователя интерсует конкретное число
# # num_user = 22
# # print(d)
# # try:
# #     print(f"{num_user} встречается {d[num_user]} раз")
# # except:
# #     print("нет такого числа нет")







# # ------------------------------------Задача------------------------------#
# У пользователей в системе есть разные уровни доступа.
# Admin:
# 	создание новых пользователей
# 	редактирование пользователей
# 	удаление пользователей
# 	блокировка пользователей

# User_active:
# 	редактирование учетной записи
# 	просмотр контента

# User_block:
# 	доступ запрещен
#
# программа получает статус, необходимо отобразить доступный функционал
#
#
# ввод
# User_blocк
#
# вывод
# доступ запрещен

# {role: [action1, action2]}

# roles_actions = {"Admin": ["создание новых пользователей",
#                            "редактирование пользователей",
#                            "удаление пользователей",
#                            "блокировка пользователей"],
#
#                  "User_active": ["редактирование учетной записи",
#                                  "просмотр контента"],
#
#                  "User_block": ["доступ запрещен"]}
# role = "User_block"
#
# try:
#     roles_actions[role]# если нет роли, то сразу попадем в блок except
#     print(role+":")
#     i = 0
#     for action in roles_actions[role]:
#         i += 1
#         print(f"\t{i}. {action}")
#
# except:
#     print("Not role")






# ------------------------------ Строки ---------------------------------- #
# строка - набор символов
# символ - все что можно использовать в печати (коды(шифры смайлков и т.д.), буквы, символы)
#
# типы символов:
#               1 буквы
#                   1.1 Заглавные буквы
#                   1.2 т.д.
#               2 цифры
#               3 пробелы (табуляция, переход строки)
#               4 спец символы
#


print(r"\n")# \ - символ    n -символ
print("\n") # \n - символ

s = "Hello world!"
print(s[0])
#s[0] = "Q" # TypeError: 'str' object does not support item assignment

# for symbol in s:
#     print(symbol)
