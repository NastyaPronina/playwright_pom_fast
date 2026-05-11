from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._first_name = page.get_by_test_id("firstName")
        self._last_name = page.get_by_test_id("lastName")
        self._zip_code = page.get_by_test_id("postalCode")
        self._continue_button = page.get_by_test_id("continue")
        self._finish_button = page.get_by_test_id("finish")
        self._success_message = page.get_by_test_id("complete-header")

    @allure.step("Заполнение формы заказа: {first_name}, {last_name}, {zip_code}")
    def fill_checkout_form(self, first_name, last_name, zip_code):
        self._first_name.fill(first_name)
        self._last_name.fill(last_name)
        self._zip_code.fill(zip_code)
        self._continue_button.click()

    @allure.step("Завершение заказа")
    def finish_order(self):
        self._finish_button.click()

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_message(self):
        return self._success_message.inner_text()