from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

    def iframe_run_command(self, command, timeout=10):
        # enable interactive shell
        self.click(self.locators.START_SHELL, timeout=10)

        # switch to main frame
        iframe = self.find(self.locators.MAIN_FRAME, timeout=timeout)
        self.driver.switch_to.frame(iframe)

        # switch to console
        console = self.find(self.locators.CONSOLE, timeout=timeout)
        self.driver.switch_to.frame(console)

        # switch to terminal
        terminal = self.find(self.locators.TERMINAL, timeout=timeout)
        self.driver.switch_to.frame(terminal)

        # wait terminal ready
        self.find(self.locators.TERMINAL_READY, timeout=timeout)

        # send command to terminal
        terminal_body = self.find(self.locators.TERMINAL_BODY)
        terminal_body.send_keys(Keys.RETURN)
        terminal_body.send_keys(Keys.RETURN)
        terminal_body.send_keys(Keys.RETURN)
        terminal_body.send_keys(command + Keys.RETURN)
