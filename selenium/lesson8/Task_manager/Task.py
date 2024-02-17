#—------------------------------- Задача —--------------------------------#
# Разработайте класс для отслеживания задач в проекте,
# хранящий информацию о статусе, исполнителе, сроках выполнения
from datetime import datetime

# вынесли is_date за пределы класса, потому, что в будущем будут добавлены еще классы, в которых потребуется такая проверка
def is_date(date):
    # initializing string
    # test_str = '04-01-1997'

    # initializing format
    format = "%d-%m-%Y"

    # checking if format matches the date
    res = True

    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(date, format))
    except ValueError:
        res = False

    return res


class Task:
    def __init__(self, author: str, expair: str, status: str = 'active'): # expair - сроках выполнения
        if is_date(expair) == False:
            # raise - прерывает выполнение программы
            raise Exception('дата должна быть в формате %d-%m-%Y') # raise - это вызов исключения
        self.author = author
        self.expair = expair # проверку является ли датой
        self.status = status

    # магические метод - перегрузки оператор
    def __repr__(self): # отображать информацию о атрибутах класса
        return f'author: {self.author}, expair: { self.expair}, status: {self.status}'

    # метод класса, который мы определили (создали)
    def show_info(self):
        return f'author: {self.author}, expair: { self.expair}, status: {self.status}'
