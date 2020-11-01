import pytest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request):
        self.client = request.getfixturevalue(
            'api_client')
