from selenium.webdriver.common.by import By


class BasePageLocators(object):
    QUERY_LOCATOR = (By.NAME, 'q')
    GO_BUTTON = (By.ID, 'submit')
    EVENTS = (By.XPATH, '//nav[@id="mainnav"]//a[@href="/events/" and contains(text(), "Events")]')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (By.XPATH, '//span[@class="comment" and contains(text(), "comprehensions")]')
    PYTHON_EVENTS = (By.XPATH, '//li[@id="events"]//a[@href="/events/python-events"]')
    INTRODUCTION = (By.CLASS_NAME, 'introduction')
    LEARN_MORE = (By.CLASS_NAME, 'readmore')

    # IFRAME
    START_SHELL = (By.ID, 'start-shell')
    MAIN_FRAME = (By.XPATH, '//iframe')
    CONSOLE = (By.ID, 'id_console')
    TERMINAL = (By.XPATH, '//iframe')
    TERMINAL_READY = (By.XPATH, '//x-row[contains(text(), ">>> ")]')
    TERMINAL_BODY = (By.XPATH, '//body')
    TERMINAL_RESULT = '//x-row[contains(text(), "{}")]'


class SearchPageLocators(BasePageLocators):
    NO_RESULTS = (By.XPATH, '//p[contains(text(), "No results found.")]')
    NO_SUCH_ELEMENT = (By.NAME, '2132132131231231231231231')


class EuroPythonEventsLocators(BasePageLocators):
    EURO_PYTHON = (By.XPATH, '//a[@href="/events/python-events/964/"]')
