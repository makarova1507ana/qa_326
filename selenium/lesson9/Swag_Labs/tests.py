from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config import *
from pages.User import *
import pytest



@pytest.fixture()
def browser():# надо переимновать
    # Перейти на указанную страницу
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    # выход из системы
    #driver.quit() # надо не закрывать Failed to establish a new connection: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение'))

# @pytest.fixture()
# def data_cases():
#     data = data_login(test_cases)
#     yield data

import time
# это тест
@pytest.mark.parametrize('username, password, expected_url', data_login(test_cases))
def test_login_page(browser, username, password, expected_url):

    # находим все элементы для заполнения
    login_page = LoginPage(browser) # browser - фикстура

    #  заполняем
    login_page.login(username, password) # username , password- параметр передается

    # ---------------если ждем адрес-------------------- #
    # wait_current_url = WebDriverWait(browser, 3)
    # res = EC.url_to_be(expected_url+'/ewe')# лучше использовать для ожидания
    # print(res(browser))# bool
    # -------------------------------------#

    #--------------------но лучше так----------------#
    #print(browser.current_url , browser.current_url == expected_url )
    # проверка на успешную авторизации
    assert browser.current_url == base_url + expected_url

def test2():
    pass

if __name__ == "__main__": # ЕСЛИ ЗАПУЩЕН ТЕКУЩИЙ МОДУЛЬ
    pytest.main([test_login_page]) # запускает test2
    # формирование отчета
    driver.quit() # после всех выполнений тестов

# input-data:
# * username = 'standard_user'
# * password = 'secret_sauce'
# expected: открытие страницы https://www.saucedemo.com/inventor.html

# input-data:
# * username = 'locked_out_user'
# * password = 'secret_sauce'
# expected: должна быть данная страницы https://www.saucedemo.com/

# input-data:
# * username = 'problem_user'
# * password = 'secret_sauce'
# expected: открытие страницы https://www.saucedemo.com/inventory.html