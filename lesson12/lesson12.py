# #----------------------------------------------------------------------#
# l = [1 ,2, 1, 1, 2, 1, 2, 22]
# unique_nums = set(l)
# d = {}
# for num in unique_nums:
#     #print(f"{num} встречается {l.count(num)}")
#     d[num] = l.count(num)
#
# max_el = max(d.values())
# print(d.values(), max(d.values()))
#
# for key in d:
#     if max_el == d[key] :
#         print(f"{key} встречается {d[key]} раз")




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


# print(r"\n")# \ - символ    n -символ
# print("\n") # \n - символ
#
# s = "Hello world!"
# print(s[0])
# #s[0] = "Q" # TypeError: 'str' object does not support item assignment
#
# # for symbol in s:
# #     print(symbol)



#----------------------------Работа со строками--------------------------#
# s = "Hello world"
# # replace (что хотим заметим(обязательно), на какой элемент(обязательно), (необязательно)сколько раз от начала необходимо выполнить замену)
# # редактирование
# s = s.replace(s[0], "1", 1)# <-- Надо делать так, а не --> так делать нельзя s[0]= "1"
# s = s.replace("l", "*", 2)
# print(s)

# #удаление
# s = "Hello world"
# s = s.replace(s[-1], "", 1)
# print(s)

#запись
# s = "Hello"
# s = s + " World!" #склейка строк (Конкатенация)
# print(s.find("*"))# -1 -потому что такого элемента нет
# print(s.find("l"))# s.find("") - возвращает индекс первого найденного элемента
# print(s.rfind("l"))# поиск с конца , но работает также как s.find("")

#print(s.index("l")) # если не знаем номер элемента, то можно узнтаь
#Можно использовать срезы [start:end:step]


s = "Hello world!"
# заменить только вторую сначала "l" на "**
#Hel + lo world! - Разбить строку на две части
# 1. найти индекс первого символа "l"
#   анализ строки со следующего индекса (сформить вторую часть)
#  и сформировать первую часть

print(s)
i1_l = s.find('l')#найти индекс первого символа "l"
print(i1_l)

part1s = s[:i1_l+1]
print(part1s)

part2_s = s[i1_l+1:]
print(part2_s)

part2_s = part2_s.replace('l','*',1)
print(part2_s)

s = part1s+part2_s

print(s)


#s = s.replace(" ", " Stdudents and ", 1)


# print(s)






