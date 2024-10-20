import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from locators.main_page_locator import MainPageLocators

BASE_URL = "https://qa-scooter.praktikum-services.ru/"
@pytest.fixture
def base_url():
    return BASE_URL

# Фикстура для инициализации драйвера
@pytest.fixture(scope="function")
def driver(base_url):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
@pytest.fixture(scope="function")
def close_cookie(driver):
    # Закрываем окно с куки, если кнопка отображается и кликабельна
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CONFIRM_COOKIE_BUTTON)).click()