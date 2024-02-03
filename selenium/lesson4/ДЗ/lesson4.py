from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time  # УДАЛИТЬ!!!


driver = webdriver.Chrome()
driver.get("https://calcus.ru/kalkulyator-ipoteki")
driver.maximize_window()
try:
    driver.implicitly_wait(5)


    property_values = driver.find_element(By.NAME, "cost")
    initial_payment = driver.find_element(By.NAME, "start_sum")
    loan_period = driver.find_element(By.NAME, "period")
    interest_rate = driver.find_element(By.NAME, "percent")
    submit_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[12]/div/input")
    test_case = {"property_values": "2600000",
                 "initial_payment": "1000000",
                 "loan_period": "5",
                 "interest_rate": "15"}
    property_values.click()
    property_values.send_keys(test_case['property_values'])
    initial_payment.click()
    initial_payment.send_keys(test_case['initial_payment'])
    loan_period.click()
    loan_period.send_keys(test_case['loan_period'])
    interest_rate.click()
    interest_rate.send_keys(test_case['interest_rate'])

    # element_to_click = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//input[@value='Рассчитать']"))
    # )
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@value='Рассчитать']"))
    # ).click()

    # wait = WebDriverWait(driver, timeout=10)
    # submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Рассчитать']")))
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 100)")
    #submit_button.click() # что-то тупит
    driver.execute_script("arguments[0].click();", submit_button)

    wait = WebDriverWait(driver, timeout=10)
    element = wait.until(EC.presence_of_element_located((By.ID, "credit-total-chart")))
    driver.execute_script("window.scrollTo(0, 100)")
    driver.save_screenshot(f'HW_6_{test_case["property_values"]}_1.png')

    driver.execute_script("window.scrollTo(0, 1200)")
    wait = WebDriverWait(driver, timeout=10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[19]/div/div/table/tbody/tr[3]")))
    # надо доджаться прогрузки анимация
    time.sleep(1)
    driver.save_screenshot(f'HW_6_{test_case["property_values"]}_2.png')

    print('Все элементы найдены!')  # оставил просто для наглядности
except NoSuchElementException:
    print("нет ни одного элемента")  # оставил просто для наглядности
