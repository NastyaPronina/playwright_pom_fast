from playwright.sync_api import Page, expect


def test_add_item_to_cart(logged_in_page):
    logged_in_page.add_first_item_to_cart()
    assert logged_in_page.get_cart_count() == "1"
    print("\nТовар успешно добавлен, в корзине 1 предмет!")


def test_item_in_cart(logged_in_page, cart_page):
    logged_in_page.add_first_item_to_cart()
    cart_page.open("https://www.saucedemo.com/cart.html")
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"

def test_full_checkout_flow(logged_in_page, cart_page, checkout_page):
    logged_in_page.add_first_item_to_cart()
    cart_page.open("https://www.saucedemo.com/cart.html")
    cart_page.click_checkout()
    checkout_page.fill_checkout_form("Ann", "Parker", "123456")
    checkout_page.finish_order()
    assert checkout_page.get_success_message() == "Thank you for your order!"
