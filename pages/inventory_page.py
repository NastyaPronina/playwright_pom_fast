from pages.base_page import BasePage
import allure

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Локатор для первой карточки товара (кнопка Add to cart)
        self._first_item_add_button = page.locator("[data-test^='add-to-cart']").first
        # Локатор иконки корзины
        self._cart_badge = page.locator("[data-test='shopping-cart-badge']")

    @allure.step("Добавление первого товара в корзину")
    def add_first_item_to_cart(self):
        self._first_item_add_button.click()

    @allure.step("Получаем количество товара в корзине")
    def get_cart_count(self):
        return self._cart_badge.inner_text()
