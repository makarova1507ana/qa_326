from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.get("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0")
# try:
#    elem = driver.find_element(By.ID, "searchInput")
#    print('Элемент нашелся')
# except NoSuchElementException:
#    print(":(")
#driver.close()

# ------------By.TAG_NAME-------------#
# try:
#    elements = driver.find_elements(By.TAG_NAME, "p")
#    print(elements, len(elements))
#    for element in elements:
#       print(element.text, '\n\n----------------------\n\n')
# except NoSuchElementException:
#    print("нет ни одного элемента")




# # --------------------------------ЗАДАНИЕ-------------------------------------- #
# # Откройте любую страницу википедии
# # Найдите любую картинку
# # Если картинка не найдена, напечатайте “нет найден элемент”
# try:
#     elements = driver.find_elements(By.TAG_NAME, "img")
#     print(f'{len(elements)} изображений есть')
#     print(elements[0].size)
# except NoSuchElementException:
#     print("нет ни одного элемента")


# ----------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------#
import time
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust")
try:
    ### НЕ НАДО ТАК #time.sleep(5) # все 5 секунд программа ждет # дождаться пока страница будет загружена

    # Дождание загрузки DOM
    #driver.implicitly_wait(5) #если страница загрузилась на 2 секунде, то мы СРАЗУ продолжим исполнять
    #если 5 секунд прошло и DOM не был полностью загружен, то программа продолжит свое исполнение

    wait = WebDriverWait(driver, timeout=10)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    form_elements = driver.find_elements(By.TAG_NAME, 'input')# страница еще не была загружена
    firstName = form_elements[0] # ошибка
    lastName = form_elements[1]
    postCode = form_elements[2]
    testCase = {"firstName": "User1",
                "lastName": "User1",
                "postCode": "1"} # брать данные из таблиц, текстовых и т.д.
    firstName.click() #firstName - объект класс webElement
    firstName.send_keys(testCase['firstName'])
    lastName.click()
    lastName.send_keys(testCase['lastName'])
    postCode.click()
    postCode.send_keys(testCase['postCode'])
    driver.save_screenshot(f'{testCase["firstName"]}.png')
except NoSuchElementException:
    print("нет ни одного элемента")




# def see_page():
#     print("see page")
# def add_products_to_card(product):
#     print(f'{product} add to card')
#
# client = {"name": 'client1', 'age': 25, 'actions': [see_page()]}



# class Cat:
#     def __init__(self, name, age): # инциализатор - запись характеристик
#         self.name = name #self.name -> поле == свойство == атрибут  характеристика
#         self.age = age #self.age -> поле == свойство == атрибут  характеристика
#
# my_cat = Cat(name="Barsik", age=2) # my_cat -> объект == экзмепляр класс Cat
# print(f"name: {my_cat.name}, age: {my_cat.age}")
#
# friend_cat = Cat(name="Vasya", age=5) # friend_cat -> объект == экзмепляр класс Cat
# print(f"name: {friend_cat.name}, age: {friend_cat.age}")




