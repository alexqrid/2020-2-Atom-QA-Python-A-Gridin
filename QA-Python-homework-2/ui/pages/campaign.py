import time
from selenium.webdriver.common.by import By
from ui.pages.main import MainPage


class CampaignPageLocators:
    CREATE_FORM_LOCATOR = (By.XPATH,
                           '//div[contains(text(),"Создать кампанию")]')
    CAMPAIGN_PURPOSE_LOCATOR = (By.XPATH,
                                '//div[contains(@class,"traffic")]')

    CAMPAIGN_NAME_LOCATOR = (By.XPATH,
                             '//div[contains(@class,'
                             '"input_campaign-name")]//input')

    CAMPAIGN_URL_LOCATOR = (By.XPATH,
                            '//input[@placeholder="Введите ссылку"]')

    CAMPAIGN_TITLE_LOCATOR = (By.XPATH,
                              '//input[@maxlength=255]')

    CAMPAIGN_FORMAT_LOCATOR = (By.ID,
                               'patterns_4')

    IMAGE_INPUT_LOCATOR = (By.XPATH,
                           '//input[@data-test="image_240x400"]')

    IMAGE_SUBMIT_LOCATOR = (By.XPATH,
                            '//input[@type="submit"]')

    CREATE_CAMPAIGN_LOCATOR = (By.XPATH,
                               '//div[contains(text(),"Создать кампанию")]')

    EXISTING_CAMPAIGN_LOCATOR = (By.XPATH,
                                 '//div[contains(@class,"NameCell")]')


class CampaignPage(MainPage):
    locators = CampaignPageLocators
    purpose = "for test"
    url = "example.com"
    title = "Test"

    def create_campaign(self,
                        url="example.com", title="Test",
                        image_path="../../static/campaign.png"):
        title_name = title

        self.click(self.locators.CREATE_FORM_LOCATOR)

        self.click(self.locators.CAMPAIGN_PURPOSE_LOCATOR)
        self.find(self.locators.CAMPAIGN_URL_LOCATOR).send_keys(url)
        self.click(self.locators.CAMPAIGN_NAME_LOCATOR)
        self.find(self.locators.CAMPAIGN_NAME_LOCATOR).send_keys(title_name)
        # после этого открывается полная форма создания и там тоже есть
        # поле "Название кампании"
        # лень было хардкодить 2 xpath-а для обоих полей названия кампании
        # поэтому при записи названия во второе поле, по сути
        # оно присваивается обоим полям
        element = self.find(self.locators.CAMPAIGN_TITLE_LOCATOR)
        element.clear()
        element.send_keys(title_name)

        self.click(self.locators.CAMPAIGN_FORMAT_LOCATOR)
        self.find(self.locators.IMAGE_INPUT_LOCATOR).send_keys(image_path)
        self.click(self.locators.IMAGE_SUBMIT_LOCATOR)
        time.sleep(1)
        self.click(self.locators.CREATE_CAMPAIGN_LOCATOR)
        # проверяем создание кампании
        xpath = f'//a[@title="{title_name}"]'
        self.find((By.XPATH, xpath), timeout=15)
        return True
