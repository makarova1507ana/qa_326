# -----------------------Задача-----------------------------#
# Создайте класс, представляющий продукт в магазине,
# хранящий информацию о его названии, цене, количестве на складе и категории
# добавьте методы просмотр товара, скидка (размер скидки)
class Product:
    def __init__(self, name: str, price: int, count: int, category: str):
        self.name = name
        self.price = price
        self.count = count
        self.category = category

    def __repr__(self):
        return f"name: {self.name}\nprice: {self.price}\ncount: {self.count}\ncategory: {self.category}\n"

    def discount(self, procent):
        if not (type(procent) in [int, float]):
            raise Exception('процент должен быть числом ')
        elif procent <= 0:
            raise Exception('процент должен быть числом больше 0')
        return self.price * (100 - procent) / 100


