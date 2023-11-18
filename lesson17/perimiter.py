"""
Написать функцию для вычисления периметра
n-угольника(проверку на существование фигуры прописать
отдельную(ые) функцию(и)), применить эту функцию(и))
для вычисления периметра n-угольника
"""

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


def P_N_angle(sides):
    # блок проверок
    if is_valid_polygon(sides):
        return sum(sides)
    return 0
