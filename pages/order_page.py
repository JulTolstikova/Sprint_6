import allure

from pages.base_page import BasePage
from locators.order_page_locator import OrderPageLocators
from locators.main_page_locator import MainPageLocators

class OrderPage(BasePage):
    @allure.step('Создаем заказ')
    def set_order(self, name, last_name, adress, phone, comment, order_button):
        name_locator = OrderPageLocators.INPUT_LOCATOR[0],OrderPageLocators.INPUT_LOCATOR[1].format("* Имя")
        last_name_locator = OrderPageLocators.INPUT_LOCATOR[0],OrderPageLocators.INPUT_LOCATOR[1].format("* Фамилия")
        adress_locator = OrderPageLocators.INPUT_LOCATOR[0],OrderPageLocators.INPUT_LOCATOR[1].format("* Адрес: куда привезти заказ")
        phone_locator = OrderPageLocators.INPUT_LOCATOR[0],OrderPageLocators.INPUT_LOCATOR[1].format("* Телефон: на него позвонит курьер")
        date_locator = OrderPageLocators.INPUT_LOCATOR[0],OrderPageLocators.INPUT_LOCATOR[1].format("* Когда привезти самокат")
        comment_locator = OrderPageLocators.INPUT_LOCATOR[0],OrderPageLocators.INPUT_LOCATOR[1].format("Комментарий для курьера")

        self.click_to_element(order_button)
        self.add_text_to_element(name_locator, name)
        self.add_text_to_element(last_name_locator, last_name)
        self.add_text_to_element(adress_locator, adress)
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_to_element(OrderPageLocators.METRO_STATION_SELECT)
        self.add_text_to_element(phone_locator, phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        self.click_to_element(date_locator)
        self.click_to_element(OrderPageLocators.TODAY_DATE_LOCATOR)
        self.click_to_element(OrderPageLocators.DAY_ORDERS_LOCATOR)
        self.click_to_element(OrderPageLocators.DAY_OPTION_LOCATOR)
        self.click_to_element(OrderPageLocators.COLOUR_GREY_CHECKBOX)
        self.add_text_to_element(comment_locator, comment)
        self.click_to_element(OrderPageLocators.MAKE_ORDER_LOCATOR)
        self.click_to_element(OrderPageLocators.APPROOVE_BUTTON)

    @allure.step('Проверяем, что заказ создался')
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.SUCCESS_ORDER_TITLE)