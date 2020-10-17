from .base import BasePage
from ui.locators.locators import BadSSL


class BadSSLPage(BasePage):
    locators = BadSSL()
