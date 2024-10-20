import allure
import pytest

from pages.order_page import OrderPage
from data import expected_text
from locators.header_page_locator import HeaderPageLocators
from locators.main_page_locator import MainPageLocators

class TestOrderPage:

    @pytest.mark.parametrize(
        'name, last_name, adress, phone, comment, order_button',
        [
            ('ТестПервый', 'Васильев', 'Москва, ул.Ленина, д.1', '89117655676', 'Тест заказа первый', HeaderPageLocators.HEADER_ORDER_BUTTON),
            ('ТестВторой', 'Иванов', 'Санкт-Петербург, ул.Ленина, д.1', '+79117655676', 'Тест заказа второй', MainPageLocators.MAIN_ORDER_BUTTON)
        ]
    )
    @allure.description(
        'Проверяем, что заказ успешно создан')
    def test_sucess_order(self, driver, close_cookie, name, last_name, adress, phone, comment, order_button):
        order_page = OrderPage(driver)
        order_page.set_order(name,last_name,adress,phone,comment, order_button)
        assert expected_text in order_page.check_order()