import allure
import pytest
from data.credentials import Credentials


@allure.title("Интеграционный тест: Данные из API JSONPlaceholder -> UI SauceDemo")
def test_checkout_with_api_data(playwright, logged_in_page, cart_page, checkout_page):
    # получаем данные клиента через API (имитируем внешнюю базу данных)
    api_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
    response = api_context.get("/users/1")
    user_api_data = response.json()

    # Подготовка данных из JSON 
    full_name_list = user_api_data["name"].split()
    first_name = full_name_list[0]
    last_name = full_name_list[1]
    zip_code = user_api_data["address"]["zipcode"]

    # Используем эти данные в UI-сценарии
    # Добавляем товар
    logged_in_page.add_first_item_to_cart()
    # Переходим в корзину и на чекаут
    cart_page.open()
    cart_page.click_checkout()

    # Заполняем форму данными, которые получили из API
    checkout_page.fill_checkout_form(first_name, last_name, zip_code)
    checkout_page.finish_order()

    assert checkout_page.get_success_message() == "Thank you for your order!"
    print(f"\nТест завершен! Данные из API: {first_name} {last_name} ({zip_code}) успешно подставлены в UI.")