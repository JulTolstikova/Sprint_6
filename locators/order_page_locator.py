from selenium.webdriver.common.by import By
class OrderPageLocators:
    INPUT_LOCATOR = By.XPATH, "//input[@placeholder = '{}']"
    METRO_STATION_INPUT = By.CSS_SELECTOR, ".select-search__value"
    METRO_STATION_SELECT = By.XPATH, "//button[@value = '5']"
    SUCCESS_ORDER_TITLE = By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"
    NEXT_BUTTON_LOCATOR = By.XPATH, "//button[text()='Далее']"
    TODAY_DATE_LOCATOR = By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"
    DAY_ORDERS_LOCATOR = By.CSS_SELECTOR, ".Dropdown-control"
    DAY_OPTION_LOCATOR = By.XPATH, "//div[@class = 'Dropdown-option']"
    COLOUR_GREY_CHECKBOX = By.XPATH, "//input[@id = 'grey']"
    MAKE_ORDER_LOCATOR = By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    APPROOVE_BUTTON = By.XPATH, "//button[text()='Да']"