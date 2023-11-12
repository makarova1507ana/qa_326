import functools

# # ----------------  reduce() ------------------------ #
# # посчитать произведение всех чисел в списке
# nums = [2, 1, 1, 1, 1, 1]
# result = functools.reduce(lambda x1, x2: x1 * x2, nums)
# print(result)






# ------------------ Задание ---------------------- #
# Дан список чисел. Проверить что это последовательность
# является геометрической и
# найти сумму геометрической прогрессии
# 2 4 8 16 32
# 30 3 0.3 0.03 ...

nums = [2, 4, 8, 16, 32]
indexes = range(len(nums))
d = nums[1] / nums[0]
check_division = lambda num1, num2: num1 * d == num2
def check_progression(nums):
    for i in range(len(nums)-1):
        if check_division(nums[i], nums[i+1]) == False:
            return False
    return True


# if check_progression(nums):
#     result = functools.reduce(lambda num1, num2: num1 + num2, nums)
#     print(result)
# else:
#     print("no progression")



# # ------------------ Задание ---------------------- #
# # Дана строка.
# # Дается разделитель
# # необходимо найти самый длинную получившуюся последовательность
#
# # "Hello kitty!"
# # kitty
# # ["Hello ",  "!"]
# # "Hello "
#
# s = "Hello kitty! kittyAeljnnlo kitty1ello "
# separator = "kitty"
# s = s.split(separator)
#
# lengths = list(map(lambda s1: len(s1), s)) # список длин
# max_length = max(lengths) # максимальную длину
# s = list(filter(lambda s1: len(s1) == max_length, s)) # оставили только те строки где длина соответствует максимальной
# print(s)








# # ------------------ Файлы ---------------------- #
# Текстовые файлы (и все, что можно преобразовать к тексту) .txt .docx, .xlsx, .json  и т.д.
# Текстовые файлы -> преобразует к строке (списку строку)

#  Бинарные файлы (все то, что нельзя преобразовать к тексту) .mp3 .png .mp4 и т.д.

# Зачем?
# 1. Хранить данные

# 2. Сохранить новые данные
# 3. Чтение

# # ------------------ Работа с файлами ---------------------- #
# 1 открыть файл -
# 2 сделать что хотели
# 3 закрыть файл -


#-------------read file-------------#
# f = open("example.txt", 'r') #open("path", mode = права доступа)
# print(f.read()) # f.read() -> str
# f.seek(0) #перемещаем указатель в начальное положение
# print(f.readlines()) # f.readlines() -> [str, str]
# f.close()


# #------------write to file---------------#
# f = open("example.txt", 'r+') #open("path", mode = права доступа)
# # size = len(f.read())
# # f.seek(size) в конце файла сделать запись и обязательно в таком режимы r+
# f.write("gg") # str -> f.write -> перезапишет file.txt
#
# f.close()



# #------------write to file---------------#
# f = open("example.txt", 'r+') #open("path", mode = права доступа)
#
# f.write("gg") # str -> f.write -> добавит изменения в начало  file.txt  и обязательно 'r+'
#
# f.close()




#
# f = open("example.txt", 'r+') #open("path", mode = права доступа)
# lines = f.readlines()
# lines[0] = "****************************************" + lines[0]
# f.seek(0)
# f.writelines(lines) # [str, str] -> f.writelines
# f.close()



def is_valid_triangle(a:int , b:int, c:int):
    return a + b > c and a + c > b and c + b > a

#--------------------Задача----------------------------#
#  в файле у вас содержатся строки такого формата
#  0, 0, 0
#  0, 0, 0
#  ...
#  0, 0, 0

# на выход
# {"line1": True, "line2": False ...}


# в любом случае за нас закроет поток
with open("example.txt", 'r') as f:
    lines = f.read().split('\n')

def test_f(lines):
    lines = list(map(lambda line: tuple(line.split(', ')), lines))
    result = {}
    for i in range(len(lines)):
        result["line"+str(i+1)] = is_valid_triangle(int(lines[i][0]), int(lines[i][1]), int(lines[i][2]))
    return result


print(test_f(lines))










