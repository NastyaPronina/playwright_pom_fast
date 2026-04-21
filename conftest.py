import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.credentials import Credentials

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def logged_in_page(login_page, inventory_page):
    login_page.open(Credentials.BASE_URL)
    login_page.login(Credentials.USERNAME, Credentials.PASSWORD)
    return inventory_page 

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)  