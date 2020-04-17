#! python3
# Rub-Us.py - Скрипт сворований с канала Гоша Дударь, который проверяет курс доллара каждые n секунд.


import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import time  # Модуль для остановки программы

TIME_TO_CHECK = 60  # Время через которое будет производится запрос


# Основной класс
class Currency:
    # Ссылка на нужную страницу
    DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+' \
                 '%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+' \
                 '%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&aqs=chrome..69i57j0l7.3430j1j7&sourceid=chrome&ie=UTF-8'
    # Заголовки для передачи вместе с URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    current_converted_price = 0
    difference = 2

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    # Метод для получения курса валюты
    def get_currency_price(self):
        # Парсим всю страницу
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_page.content, 'lxml')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    # Проверка изменения валюты
    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
            print("Сейчас курс: 1 доллар = " + str(currency))

        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")
            print("Сейчас курс: 1 доллар = " + str(currency))

        change_float = currency - self.current_converted_price
        print("|-|-|Сейчас курс: 1 $ = " + str(currency), "\n Изменился на: ", round(change_float, 2))
        time.sleep(TIME_TO_CHECK)  # Засыпание программы на TIME_TO_CHECK
        self.check_currency()


# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()
