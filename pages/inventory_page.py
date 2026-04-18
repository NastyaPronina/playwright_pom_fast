from pages.base_page import BasePage
import allure

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Локатор для первой карточки товара (кнопка Add to cart)
        self._first_item_add_button = page.locator("[data-test^='add-to-cart']").first
        # Локатор иконки корзины
        self._cart_badge = page.locator("[data-test='shopping-cart-badge']")
        # Локатор для кнокпки Remove
        self._remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")
        # Локатор выпадающего списка (селектора)
        self._sort_dropdown = page.locator("[data-test='product-sort-container']")
        # Локатор для всех цен на странице
        self._item_prices = page.locator("[data-test='inventory-item-price']")

    @allure.step("Добавление первого товара в корзину")
    def add_first_item_to_cart(self):
        self._first_item_add_button.click()

    @allure.step("Получаем количество товара в корзине")
    def get_cart_count(self):
        return self._cart_badge.inner_text()

    @allure.step("Удаление товара из корзины через страницу каталога")
    def remove_first_item(self):
        self._remove_button.click()

    def is_remove_button_visible(self):
        # Проверяем, видна ли кнопка удаления (возвращает True/False)
        return self._remove_button.is_visible()

    @allure.step("Сортировка товаров по цене: от низкой к высокой")
    def sort_by_price_low_to_high(self):
        # В <select> выбираем значение напрямую
        self._sort_dropdown.select_option("lohi")

    def get_all_prices(self):
        # Находим все элементы цен
        price_elements = self._item_prices.all_inner_texts()
        return [float(p.replace('$', '')) for p in price_elements]