from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.europython_events import EuroPythonEventsPage


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_europython_events(self):
        events = self.find(self.locators.EVENTS)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.wait().until(EC.element_to_be_clickable(self.locators.PYTHON_EVENTS))
        self.click(self.locators.PYTHON_EVENTS)

        return EuroPythonEventsPage(self.driver)


