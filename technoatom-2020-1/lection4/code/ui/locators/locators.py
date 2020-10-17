from selenium.webdriver.common.by import By


class BaseLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    NO_SUCH_ELEMENT = (By.NAME, '2132132131231231231231231')
    GO_BUTTON = (By.ID, 'submit')
    DOWNLOADS_BUTTON = (By.XPATH, '//li[@id="downloads"]//a[@href="/downloads/" and contains(text(), "Downloads")]')
    ALL_RELEASES = (By.XPATH, '//a[@href="/downloads/" and contains(text(), "All releases")]')
    EVENTS = (By.XPATH, '//nav[@id="mainnav"]//a[@href="/events/" and contains(text(), "Events")]')
    PYTHON_EVENTS = (By.XPATH, '//li[@id="events"]//a[@href="/events/python-events"]')


class MainPageLocators(BaseLocators):
    COMPREHENSIONS = (By.XPATH, '//span[@class="comment" and contains(text(), "comprehensions")]')
    INTRODUCTION = (By.CLASS_NAME, 'introduction')
    LEARN_MORE = (By.CLASS_NAME, 'readmore')
    NO_RESULTS = (By.XPATH, '//p[contains(text(), "No results found.")]')

    # Iframe
    START_SHELL = (By.ID, 'start-shell')
    MAIN_FRAME = (By.XPATH, '//iframe')
    CONSOLE = (By.ID, 'id_console')
    TERMINAL = (By.XPATH, '//iframe')
    TERMINAL_READY = (By.XPATH, '//x-row[contains(text(), ">>> ")]')
    TERMINAL_BODY = (By.XPATH, '//body')
    EXPECTED_MSG = (By.XPATH, '//x-row[contains(text(), "ZeroDivisionError")]')
    IFRAME_BODY = (By.XPATH, '//body')
    IFRAME_RESULT = '//x-row[contains(text(), "{}")]'


class DownLoadPageLocators(BaseLocators):
    PYTHON_TEMPLATE = '//a[contains(text(), "Python {}")'


class PythonLocators382(BaseLocators):
    WINDOWS_X86_X64_WEB_BASED = (By.XPATH, '//*[contains(text(), "Windows x86-64 web-based installer")]')


class PythonEventsLocators(BaseLocators):
    EURO_PYTHON = (By.XPATH, '//a[@href="/events/python-events/875/"]')


class BadSSL(BaseLocators):
    H1_CONTENT = (By.XPATH, '//*[@id="content"]/h1')
