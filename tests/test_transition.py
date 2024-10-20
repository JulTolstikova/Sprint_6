import allure
from pages.transition_page import TransitionPage
from data import main_title_text, dzen_logo_text

class TestTransition:
    @allure.description(
        'Проверяем, что осуществляется переход по лого Самокат')
    def test_scooterlogo_transition(self, driver, close_cookie):
        transition_page = TransitionPage(driver)
        assert main_title_text in transition_page.check_scooterlogo_transition()

    @allure.description(
        'Проверяем, что осуществляется переход по лого Яндекс')
    def test_yandexlogo_transition(self, driver, close_cookie):
        transition_page = TransitionPage(driver)
        assert transition_page.check_yandex_transition is not None