# Playwright Automation Project (SauceDemo)

Это учебный проект по автоматизации тестирования UI-интерфейса сайта [SauceDemo](https://saucedemo.com).

## Стек технологий
* **Python** 
* **Playwright** (библиотека для автоматизации)
* **Pytest** (тест-раннер)
* **Page Object Model (POM)** (архитектура)

## Реализованные проверки
- [x] Авторизация (позитивные и негативные сценарии с параметризацией).
- [x] Добавление товаров в корзину.
- [x] Полный сквозной процесс оформления заказа (End-to-End).

## Как запустить проект

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/NastyaPronina/playwright_pom_fast.git
   cd playwright_pom_fast

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Mac/Linux
    .\venv\Scripts\activate   # Для Windows

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    playwright install

4. Запустите тесты:
    ```bash
    pytest  
