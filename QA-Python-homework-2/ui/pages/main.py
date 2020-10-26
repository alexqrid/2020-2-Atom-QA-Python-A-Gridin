from selenium.common.exceptions import StaleElementReferenceException, \
    TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

RETRY_COUNT = 15


class MainPageLocators:
    LOGIN_FORM_LOCATOR = (By.XPATH, '//div[contains(text(), "Войти")]')
    EMAIL_LOCATOR = (By.XPATH, '//input[@name="email"]')
    PASSWORD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    LOGIN_LOCATOR = (By.XPATH, '//div[contains(@class,"authForm") and '
                               'contains(text(),"Войти")]')
    USERNAME_LOCATOR = (By.XPATH, '//div[contains(@class,'
                                  '"right-module-userName")]')


class MainPage:
    locators = MainPageLocators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=10,
             wait_for=EC.presence_of_element_located) -> WebElement:
        # нотация WebElement удобна тем, что у метода find становятся
        # доступны методы WebElement а это очень удобно
        return self.wait(timeout).until(
            wait_for(locator))

    def click(self, locator, timeout=10):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i > RETRY_COUNT - 1:
                    pass
                raise

    def login(self, creds):
        self.click(self.locators.LOGIN_FORM_LOCATOR)
        self.find(self.locators.EMAIL_LOCATOR).send_keys(
            creds['email'])

        self.find(self.locators.PASSWORD_LOCATOR).send_keys(
            creds['password'] + Keys.RETURN)

    def is_authenticated(self, timeout=5):
        try:
            self.find(self.locators.USERNAME_LOCATOR, timeout)
        except TimeoutException:
            return False
        return True
