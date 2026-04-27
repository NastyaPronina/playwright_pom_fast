from playwright.sync_api import Page, expect


@allure.title("Тест на наличие 'Swag Labs' в заголовке")
def test_check_sauce_demo(page: Page):
    # Открываем сайт
    page.goto("https://saucedemo.com")
    # Проверяем, что в заголовке есть текст Swag Labs
    expect(page).to_have_title("Swag Labs")
    print("\nБраузер успешно открылся и заголовок совпал!")
