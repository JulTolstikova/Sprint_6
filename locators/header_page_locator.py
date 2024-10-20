from selenium.webdriver.common.by import By
class HeaderPageLocators:
    YANDEX_LOGO = By.XPATH, "//a[@href='//yandex.ru']"
    SCOOTER_LOGO = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    HEADER_ORDER_BUTTON = By.XPATH, "//button[@class = 'Button_Button__ra12g']"