import pytest
import uuid

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.audience import AudiencePage
from ui.pages.campaign import CampaignPage
from ui.pages.dashboard import DashboardPage
from ui.pages.main import MainPage


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope="session", autouse=True)
def credentials():
    try:
        from local_config import credentials
    except ImportError:
        import os
        credentials = {"email": os.getenv("LOGIN_EMAIL"),
                       "password": os.getenv("LOGIN_PASS")}
    return credentials


@pytest.fixture
def authenticate(driver, main_page, credentials):
    logged_page = main_page
    logged_page.login(credentials)
    return DashboardPage(logged_page.driver)


@pytest.fixture
def campaign_page(driver):
    page = CampaignPage(driver)
    return page


@pytest.fixture
def dashboard_page(driver):
    page = DashboardPage(driver)
    return page


@pytest.fixture
def audience_page(driver):
    page = AudiencePage(driver)
    return page


@pytest.fixture
def unique():
    temp = uuid.uuid1()
    return temp.hex


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']
    selenoid = config['selenoid']
    headless = config['headless']
    if browser == 'chrome':
        options = ChromeOptions()
        if selenoid:
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "86.0",
                "selenoid:options": {
                    "enableVNC": False,
                    "enableVideo": False
                }
            }

            driver = webdriver.Remote(command_executor=selenoid,
                                      options=options,
                                      desired_capabilities=capabilities
                                      )
        else:
            options.add_argument("--window-size=800,600")
            options.add_argument(
                "--no-sandbox")  # This make Chromium reachable
            options.add_argument(
                "--no-default-browser-check")  # Overrides default choices
            options.add_argument("--no-first-run")
            options.add_argument("--disable-default-apps")
            if headless:
                options.add_argument('--headless')
            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)

            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={
                                          'acceptInsecureCerts': True}
                                      )
    else:
        raise UnsupportedBrowserException(f'Unsupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver

    # quit = закрыть страницу, остановить browser driver
    # close = закрыть страницу, бинарь browser driver останется запущенным
    driver.quit()
