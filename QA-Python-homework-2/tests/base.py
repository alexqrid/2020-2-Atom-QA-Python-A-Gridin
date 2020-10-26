import pytest
from _pytest.fixtures import FixtureRequest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.main_page = request.getfixturevalue('main_page')
        self.dashboard = request.getfixturevalue('dashboard_page')
        self.campaign = request.getfixturevalue('campaign_page')
        self.audience = request.getfixturevalue('audience_page')
