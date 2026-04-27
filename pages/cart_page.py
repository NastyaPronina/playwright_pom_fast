from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    RELATIVE_URL = "/cart.html"

    def __init__(self, page):
        super().__init__(page)
        self._cart_item_name = page.locator("[data-test='inventory-item-name']").first
        self._checkout_button = page.locator("[data-test='checkout']")

    @allure.step("Получение названия товара в корзине")
    def get_cart_item_name(self):
        return self._cart_item_name.inner_text()

    @allure.step("Нажатие на кнопку 'Checkout' в корзине")
    def click_checkout(self):
        self._checkout_button.click()
