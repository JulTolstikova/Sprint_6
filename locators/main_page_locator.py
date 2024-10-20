from selenium.webdriver.common.by import By
class MainPageLocators:
    CONFIRM_COOKIE_BUTTON = By.XPATH, "//button[text()='да все привыкли']"
    QUESTION_LOCATOR = By.XPATH, "//*[@id = 'accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//*[@id = 'accordion__panel-{}']"
    QUESTION_LOCATOR_7 = By.ID, 'accordion__heading-7'
    MAIN_ORDER_BUTTON = By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"