from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Инициализация драйвера (вам нужно подставить свой путь к драйверу)
driver = webdriver.Chrome()

driver.get("file:///C:/Users/Anastasia/Desktop/Groups/QA_326/OAT/selenium/lesson6/css_selector/css_selectot.html")

try:
    # Использование CSS-селектора для поиска кнопки
    button = driver.find_element(By.CSS_SELECTOR,"body > div > button")#"body div button")

    # Печать сообщения о том, что элемент был найден
    print("Элемент найден:", button.text)

    # Использование CSS-селектора для поиска кнопки
    first_element_of_list = driver.find_element(By.CSS_SELECTOR,"#myList > li:nth-child(1)")

    # Печать сообщения о том, что элемент был найден
    print("Элемент найден:", first_element_of_list.text)

except NoSuchElementException:
    # Обработка исключения, если элемент не найден
    print("Элемент не найден")

finally:
    driver.quit()
