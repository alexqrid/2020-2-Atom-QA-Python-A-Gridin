from selenium.webdriver.common.by import By
from ui.pages.main import MainPage


class DashboardPageLocators:
    CAMPAIGN_LOCATOR = (By.XPATH, '//a[@href="/dashboard"]')
    AUDITORY_LOCATOR = (By.XPATH, '//a[@href="/segments"]')
    USERNAME_LOCATOR = (By.XPATH, '//div[contains(@class,'
                                  '"right-module-userName")]')


class DashboardPage(MainPage):
    locators = DashboardPageLocators

    def go_to_campaign(self):
        self.click(self.locators.CAMPAIGN_LOCATOR)

    def go_to_audience(self):
        self.click(self.locators.AUDITORY_LOCATOR)
