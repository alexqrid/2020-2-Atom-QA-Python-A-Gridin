import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tests.base import BaseCase
from ui.locators import basic_locators


class Test(BaseCase):

    @pytest.mark.skip(reason='TEMP')
    def test_basic(self):
        assert 'Python' in self.driver.title

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.parametrize('query', ['pycon', 'python'])
    def test_search(self, query):
        self.search(query)
        assert "No results found." not in self.driver.page_source

    @pytest.mark.skip(reason='TEMP')
    def test_search_negative(self):
        self.search('23132173152361253675216735126735132516736712')
        self.find(basic_locators.NO_RESULTS).is_displayed()

    @pytest.mark.skip(reason='TEMP')
    def test_carousel(self):
        self.click(basic_locators.COMPREHENSIONS, timeout=12)

    @pytest.mark.skip(reason='TEMP')
    def test_count(self):
        with pytest.raises(TimeoutException):
            self.count_elements(basic_locators.NO_SUCH_ELEMENT, count=2)

    @pytest.mark.skip(reason='TEMP')
    def test_euro_python(self):
        events = self.find(basic_locators.EVENTS)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.click(basic_locators.PYTHON_EVENTS)
        self.click(basic_locators.EURO_PYTHON)

        assert 'Dublin' in self.driver.page_source

    @pytest.mark.skip(reason='TEMP')
    def test_page_changed(self):
        self.click(basic_locators.GO_BUTTON)

    @pytest.mark.skip(reason='TEMP')
    def test_relative(self):
        intro = self.find(basic_locators.INTRODUCTION)
        learn_more = intro.find_element(*basic_locators.LEARN_MORE)

        if self.config['url'].startswith('https'):
            expected = self.config['url']
        else:
            expected = self.config['url'].replace('http', 'https')

        assert learn_more.get_attribute('href') == f'{expected}/doc/'

    @pytest.mark.skip(reason='TEMP')
    def test_options(self):
        self.driver.get('https://expired.badssl.com/')
        self.find((By.XPATH, '//*[@id="content"]/h1'))

    def test_download(self):
        self.driver.get('https://www.python.org/downloads/release/python-382/')
        self.click((By.XPATH, '//*[contains(text(), "Windows x86-64 web-based installer")]'))

        self.wait_download('python-3.8.2-amd64-webinstall.exe')
