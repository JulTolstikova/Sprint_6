from selenium.webdriver.common.by import By
class TransitionPageLocators:
    MAIN_TITLE = By.XPATH, "//div[@class = 'Home_Header__iJKdX']"
    CHECK_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"
    DZEN_LOCATORS = (By.ID, "dzen-header")