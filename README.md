28.1. Тестирование требований к форме авторизации ЛК Ростелеком (https://b2c.passport.rt.ru)
Запуск тестов
1. Файлы из репозотория скопировать на компьютер
2. Установить требования:
    pip install -r requirements.txt
3. Загрузить Selenium WebDriver с https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)
4. Запустить тесты:
     python -m pytest -v --driver Chrome --driver-path webdriver/chromdriver.exe tests/test_rostelecom.py

