import allure
from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators
class MainPage(BasePage):

    @allure.step('Кликаем на вопрос')
    def click_to_question(self, locator_q_formatted):
        locator_7_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, 7)
        self.scroll_to_element(locator_7_formatted)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст с ответа')
    def get_answer_text_1(self, locator_a_formatted):
        return self.get_text_from_element(locator_a_formatted)

    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_7)
        self.click_to_question(locator_q_formatted)
        return self.get_answer_text_1(locator_a_formatted)