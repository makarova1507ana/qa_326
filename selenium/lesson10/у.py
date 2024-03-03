import requests  # Импорт библиотеки для отправки HTTP запросов

url = "https://hh.ru" # Адрес исследуемого сайта
print(url) # Вывод ссылки на печать (для контроля)
result = requests.get(url) # Поместили наш запрос с методом GET
print("статус код : " + str(result.status_code)) # Вывод на печать статус кода
assert 200 == result.status_code # Проверка кода
if result.status_code == 200: # Условия,если статус код 200
  print("Успешно") # Выводим запись "Успешно"
else:
    print ("Провал") # В другом случае "Провал"
result.encoding = "utf-8" # Кодировка
with open("resultHTML.html", "w", encoding="utf-8") as f:
    f.write(result.text) # Выводим на печать наш ответ