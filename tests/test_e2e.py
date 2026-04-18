from playwright.sync_api import Page, expect
import allure


@allure.title("Тест на добавление первого в списке товара в корзину")
def test_add_item_to_cart(logged_in_page):
    logged_in_page.add_first_item_to_cart()
    expect(logged_in_page._cart_badge).to_have_text("1")
    print("\nТовар успешно добавлен, в корзине 1 предмет!")

@allure.title("Тест на наличие товара в корзине")
def test_item_in_cart(logged_in_page, cart_page):
    logged_in_page.add_first_item_to_cart()
    cart_page.open("https://www.saucedemo.com/cart.html")
    expect(cart_page._cart_item_name).to_have_text("Sauce Labs Backpack")

@allure.title("Тест на совершение заказа товара")
def test_full_checkout_flow(logged_in_page, cart_page, checkout_page):
    logged_in_page.add_first_item_to_cart()
    cart_page.open("https://www.saucedemo.com/cart.html")
    cart_page.click_checkout()
    checkout_page.fill_checkout_form("Ann", "Parker", "123456")
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


