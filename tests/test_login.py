from playwright.sync_api import Page, expect


def test_login_success(page, login_page):
    # 1. Используем методамы класса
    login_page.open("https://saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Проверяем результат (что мы перешли на страницу каталога)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


import pytest

@pytest.mark.parametrize("user, password", [
    ("locked_out_user", "secret_sauce"), # Заблокированный юзер
    ("standard_user", "wrong_password"), # Неверный пароль
    ("", "")                             # Пустые поля
])

def test_login_failure(page, login_page, user, password):
    login_page.open("https://saucedemo.com")
    
    # Пытаемся залогиниться с данными из списка выше
    login_page.login(user, password)
    
    # Проверяем, что появилось сообщение об ошибке
    # Мы обращаемся к локатору, который уже описали в LoginPage
    expect(login_page._error_message).to_be_visible()
 
