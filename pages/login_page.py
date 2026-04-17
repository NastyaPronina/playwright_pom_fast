from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page) 
        # Локаторы (находим элементы)
        self._username_field = page.locator("[data-test='username']")
        self._password_field = page.locator("[data-test='password']")
        self._login_button = page.locator("[data-test='login-button']")
        self._error_message = page.locator("[data-test='error']")

    @allure.step("Авторизация пользователем {username}")
    def login(self, username, password):
        self._username_field.fill(username)
        self._password_field.fill(password)
        self._login_button.click()
