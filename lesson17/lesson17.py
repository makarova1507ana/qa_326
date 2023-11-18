# #—------------------------------- Задача —--------------------------------#
# # Дан файл. Каждая строка содержит значение адреса объекта, стоимости покупки.
# # Найти самый дешевый, самый дорогой, показать 5 самых дорогих и
# # 5 самых дешевых
#
# #—------------------------------- кодировка —--------------------------------#
# # кодировка - система учета символов
# # ASCII, UTF-8, UTF-16
#
# import re
# # Алгоритм
# # 1. Прочитать данные и преобразовать к нужному формату [{adress: "адрес д.1 кв.1", cost: 50000}, {...}]
# with open("example.txt", 'r', encoding='UTF-8') as f:
#     objects = f.readlines() #f.readlines()  -> ['...\n', '...\n', ...]
#
#
# for i, line in enumerate(objects):
#     d = {}
#     adress = re.split(r'[ ][1-9]\d+ue\n', line)[0]
#     d['adress'] = adress
#
#     cost = int(re.findall(r'[ ][1-9]\d+', line)[0])
#     d['cost'] = cost
#
#     # d = {'adress': re.split(r'[ ][1-9]\d+ue\n', line)[0], 'cost': int(re.findall(r'[ ][1-9]\d+', line)[0])}
#     objects[i] = d
# #print(objects)
#
#
# # objects = [{'adress': "адрес д.1 кв.1", 'cost': 50000}, {...}]
# # 2.
#
# min_obj= {'adress': '', 'cost': 100000*10000}
# max_obj = {'adress': '', 'cost': 0}
#
# for obj in objects: # obj = {'adress': "адрес д.1 кв.1", 'cost': 50000}
#     #   2.1 Найти самый дешевый
#     if obj['cost'] < min_obj['cost']:
#         min_obj['cost'] = obj['cost']
#         min_obj['adress'] = obj['adress']
#
#     #   2.2 Найти самый дорогой
#     if obj['cost'] > max_obj['cost']:
#         max_obj['cost'] = obj['cost']
#         max_obj['adress'] = obj['adress']
# print(max_obj, min_obj)
#
# #   2.3 показать 5 самых дорогих
# #   2.4 показать 5 самых дешевых


#—------------------------------- Задача —--------------------------------#
# Дан файл. Каждая строка содержит произвольное значения разделенные для произвольного кол-во сторон запятой.
# Создать список, с периметрами для каждой фигуры

# as p дать локальное имя
import perimiter as p # даем доступ к файлу perimiter.py

with open('data_for_perimiter.txt', 'r') as f:
    lines = f.read() # lines = '   \n 1, 2\n ...' - > [(1, 2), ()]
    lines = lines.split('\n') # lines  = ['', '', ...]
# print(lines)


test_data = []
for line in lines: #line = '1, 2\n' -> (1, 2)


    try:
        # num = '1'
        data = tuple(map(lambda num: int(num), line.split(', ')))# line.split(', ') -> ['1', '2\n']
        test_data.append(data) # data = (1, 2)
    except:
        continue

print(test_data)
perimiters = []
for data in test_data:
    perimiters.append(p.P_N_angle(data))
print(perimiters)