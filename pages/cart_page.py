from pages.base_page import BasePage

class CartPage(BasePage):
    RELATIVE_URL = "/cart.html"

    def __init__(self, page):
        super().__init__(page)
        self._cart_item_name = page.locator("[data-test='inventory-item-name']").first
        self._checkout_button = page.locator("[data-test='checkout']")

    def get_cart_item_name(self):
        return self._cart_item_name.inner_text()

    def click_checkout(self):
        self._checkout_button.click()
