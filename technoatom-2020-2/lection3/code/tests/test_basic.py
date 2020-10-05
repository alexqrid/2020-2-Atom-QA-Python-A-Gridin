import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from tests.base import BaseCase


class Test(BaseCase):

    @pytest.mark.skip(reason='no need')
    def test_basic(self):
        assert 'Python' in self.driver.title

    @pytest.mark.skip(reason='no need')
    @pytest.mark.parametrize('query', ['pycon', 'python'])
    def test_search(self, query):
        self.base_page.search(query)
        assert "No results found." not in self.driver.page_source

    @pytest.mark.skip(reason='no need')
    def test_search_negative(self):
        self.search_page.search('23132173152361253675216735126735132516736712')
        self.search_page.find(self.search_page.locators.NO_RESULTS).is_displayed()

    @pytest.mark.skip(reason='no need')
    def test_carousel(self):
        self.main_page.click(self.main_page.locators.COMPREHENSIONS, timeout=12)

    @pytest.mark.skip(reason='no need')
    def test_count(self):
        # негативный тест, ожидаем конкретный exception, а не любой, это важно
        # проверяем что количество элементов у нас 2 на странице
        with pytest.raises(TimeoutException):
            self.base_page.count_elements(self.search_page.locators.NO_SUCH_ELEMENT, count=2)

    @pytest.mark.skip(reason='no need')
    def test_euro_python(self):
        with allure.step('Go to euro python page'):
            europython_page = self.main_page.go_to_europython_events()

        with allure.step('Click europython events'):
            europython_page.click(europython_page.locators.EURO_PYTHON)

        assert 'Dublin' in self.driver.page_source

    @pytest.mark.skip(reason='no need')
    def test_page_changed(self):
        # псевдо тест, просто чтобы можно было проверить работу метода click
        # эмулируя попытки
        self.main_page.click(self.main_page.locators.GO_BUTTON)

    @pytest.mark.skip(reason='no need')
    def test_relative(self):
        intro = self.main_page.find(self.main_page.locators.INTRODUCTION)
        learn_more = intro.find_element(*self.main_page.locators.LEARN_MORE)

        if self.config['url'].startswith('https'):
            expected = self.config['url']
        else:
            expected = self.config['url'].replace('http', 'https')

        assert learn_more.get_attribute('href') == f'{expected}/doc/'

    @pytest.mark.skip(reason='no need')
    def test_options(self):
        self.driver.get('https://expired.badssl.com/')
        self.base_page.find((By.XPATH, '//*[@id="content"]/h1'))

    @pytest.mark.skip(reason='no need')
    def test_download(self):
        self.driver.get('https://www.python.org/downloads/release/python-382/')
        self.base_page.click((By.XPATH, '//*[contains(text(), "Windows x86-64 web-based installer")]'))

        self.wait_download('python-3.8.2-amd64-webinstall.exe')

    def test_take_screenshot(self):
        """ Ненастоящий тест, показывает, как в отчет с аллюром можно положить скриншот """

        with allure.step('Go to europython page'):
            self.main_page.go_to_europython_events()

        with allure.step('Attach screenshot'):
            allure.attach(name='Europython', body=self.driver.get_screenshot_as_png(),
                          attachment_type=AttachmentType.PNG)

    def test_screenshot_on_fail(self):
        """ ненастоящий тест, делаем скриншот при неудачной загрузке страницы"""
        with allure.step('Open bad url'):
            try:
                self.driver.get("asdasdasd")
            except Exception:
                allure.attach(name='Europython', body=self.driver.get_screenshot_as_png(),
                              attachment_type=AttachmentType.PNG)

    def test_iframe(self):
        command = 'assert 1 / 0'
        expected_msg = 'ZeroDivisionError'
        locator = (By.XPATH, self.main_page.locators.TERMINAL_RESULT.format(expected_msg))

        self.main_page.iframe_run_command(command)
        assert self.main_page.find(locator)
        self.driver.switch_to.default_content()

        import time
        time.sleep(5)
