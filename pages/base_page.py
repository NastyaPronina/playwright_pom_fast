from playwright.sync_api import Page
from data.credentials import Credentials
import allure

class BasePage:
    RELATIVE_URL = ""

    def __init__(self, page: Page):
        self.page = page

    def open(self, base_url: str = Credentials.BASE_URL):
        self.page.goto(f"{base_url}{self.RELATIVE_URL}")

    def get_title(self):
        return self.page.title()

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector, state="visible")