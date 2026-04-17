import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

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
    login_page.open("https://saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    return inventory_page 

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)  