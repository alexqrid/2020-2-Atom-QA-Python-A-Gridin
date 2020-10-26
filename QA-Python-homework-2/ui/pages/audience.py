from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.main import MainPage


class AudiencePageLocators:
    CREATE_FORM_LOCATOR = (By.XPATH,
                           '//a[contains(text(),"Создайте")]')
    CREATE_FORM_LOCATOR_WHEN_EXISTS = (By.XPATH,
                                       '//button[contains(@class,'
                                       '"button_submit")]')
    CHECKBOX_LOCATOR = (By.XPATH,
                        '//input[contains(@class,"adding-segments")]')
    ADD_BUTTON_LOCATOR = (By.XPATH,
                          '//div[@class="button__text" and contains(text(),'
                          '"Добавить сегмент")]')
    CREATE_BUTTON_LOCATOR = (By.XPATH,
                             '//div[@class="button__text" and contains(text('
                             '),"Создать сегмент")]')
    SEGMENT_ALIAS_LOCATOR = (By.XPATH,
                             '//input[@type="text" and @maxlength=60]')
    SEGMENT_TITLE_LOCATOR = (By.XPATH, '//a[@title]')
    SEGMENT_REMOVE_BUTTON_LOCATOR = (By.XPATH,
                                     '//span[contains(@class,"remove")]')
    SEGMENT_REMOVE_APPROVE_BUTTON_LOCATOR = (By.XPATH,
                                             '//div[@class="button__text" '
                                             'and contains(text(),'
                                             '"Удалить")]')


class AudiencePage(MainPage):
    locators = AudiencePageLocators

    def create_audience(self, title="Test Segment"):
        try:
            self.click(self.locators.CREATE_FORM_LOCATOR_WHEN_EXISTS)
        except TimeoutException:
            self.click(self.locators.CREATE_FORM_LOCATOR)

        name = title
        self.click(self.locators.CHECKBOX_LOCATOR)

        self.click(self.locators.ADD_BUTTON_LOCATOR)
        alias = self.find(self.locators.SEGMENT_ALIAS_LOCATOR)
        alias.clear()
        alias.send_keys(name)
        self.click(self.locators.CREATE_BUTTON_LOCATOR)
        xpath = (By.XPATH, f"//a[contains(@title, \"{name}\" )]")
        self.find(xpath, timeout=15,
                  wait_for=EC.element_to_be_clickable)
        return True

    def delete_audience(self, title="Delete Segment"):
        name = title
        self.create_audience(title=name)
        locator = f'//a[@title="{name}"]/../..' \
                  '/following-sibling::*/' \
                  'following-sibling::*/' \
                  'following-sibling::*/span[contains(@class,"remove")]'

        self.click((By.XPATH, locator), timeout=20)
        self.click(self.locators.SEGMENT_REMOVE_APPROVE_BUTTON_LOCATOR)

        return True
