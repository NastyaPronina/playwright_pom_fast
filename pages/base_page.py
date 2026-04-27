from playwright.sync_api import Page
from data.credentials import Credentials
import allure

class BasePage:
    RELATIVE_URL = ""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открытие страницы")
    def open(self, base_url: str = Credentials.BASE_URL):
        self.page.goto(f"{base_url}{self.RELATIVE_URL}")

    @allure.step("Получение заголовка страницы")
    def get_title(self):
        return self.page.title()

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector, state="visible")