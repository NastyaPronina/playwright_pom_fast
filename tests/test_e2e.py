from playwright.sync_api import expect
import allure
from data.credentials import Credentials


@allure.title("Тест на добавление первого в списке товара в корзину")
def test_add_item_to_cart(logged_in_page):
    logged_in_page.add_first_item_to_cart()
    expect(logged_in_page._cart_badge).to_have_text("1")
    print("\nТовар успешно добавлен, в корзине 1 предмет!")

@allure.title("Тест на наличие товара в корзине")
def test_item_in_cart(logged_in_page, cart_page):
    logged_in_page.add_first_item_to_cart()
    cart_page.open()
    expect(cart_page._cart_item_name).to_have_text("Sauce Labs Backpack")

@allure.title("Тест на совершение заказа товара")
def test_full_checkout_flow(logged_in_page, cart_page, checkout_page):
    logged_in_page.add_first_item_to_cart()
    cart_page.open()
    cart_page.click_checkout()
    checkout_page.fill_checkout_form(
        Credentials.FIRST_NAME, 
        Credentials.LAST_NAME, 
        Credentials.ZIP_CODE)
    checkout_page.finish_order()
    expect(checkout_page._success_message).to_have_text("Thank you for your order!")

@allure.title("Тест на добавление и последующее удаление товара")
def test_add_and_remove_item(logged_in_page):
    logged_in_page.add_first_item_to_cart()
    # Проверяем, что кнопка Remove видна
    expect(logged_in_page._remove_button).to_be_visible()
    logged_in_page.remove_first_item()
    # Проверяем, что т.к. корзина пустая, то элемент 'shopping-cart-badge' отсутствует в DOM
    expect(logged_in_page._cart_badge).not_to_be_attached()

@allure.title("Проверка сортировки товаров по цене (от низкой к высокой)")
def test_sort_prices_low_to_high(logged_in_page):
    # 1. Применяем сортировку
    logged_in_page.sort_by_price_low_to_high()
    # 2. Получаем список цен со страницы (только числа)
    actual_prices = logged_in_page.get_all_prices()
    # 3. Создаем ожидаемый (отсортированный) список цен
    expected_prices = sorted(actual_prices)
    # 4. Сравниваем их между собой
    assert actual_prices == expected_prices, f"Сортировка неверная! Ожидали {expected_prices}, получили {actual_prices}"


