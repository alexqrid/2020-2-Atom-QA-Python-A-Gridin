from selenium.webdriver.common.by import By

QUERY_LOCATOR = (By.NAME, 'q')

GO_BUTTON = (By.ID, 'submit')

NO_RESULTS = (By.XPATH, '//p[contains(text(), "No results found.")]')

COMPREHENSIONS = (By.XPATH, '//span[@class="comment" and contains(text(), "comprehensions")]')

NO_SUCH_ELEMENT = (By.NAME, '2132132131231231231231231')


EVENTS = (By.XPATH, '//nav[@id="mainnav"]//a[@href="/events/" and contains(text(), "Events")]')
PYTHON_EVENTS = (By.XPATH, '//li[@id="events"]//a[@href="/events/python-events"]')
EURO_PYTHON = (By.XPATH, '//a[@href="/events/python-events/964/"]')

INTRODUCTION = (By.CLASS_NAME, 'introduction')
LEARN_MORE = (By.CLASS_NAME, 'readmore')
