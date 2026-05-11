from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page) 
        # Локаторы (находим элементы)
        self._username_field = page.get_by_test_id("username")
        self._password_field = page.get_by_test_id("password")
        self._login_button = page.get_by_test_id("login-button")
        self._error_message = page.get_by_test_id("error")

    @allure.step("Авторизация пользователем {username}")
    def login(self, username, password):
        self._username_field.fill(username)
        self._password_field.fill(password)
        self._login_button.click()
