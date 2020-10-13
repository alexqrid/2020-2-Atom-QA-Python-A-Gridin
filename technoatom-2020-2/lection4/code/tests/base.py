import pytest

from api.client import ApiClient
from conftest import Settings


class UserNotFoundException(Exception):
    pass


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request, logger):
        self.config: Settings = config
        self.api_client: ApiClient = request.getfixturevalue('api_client')
        self.logger = logger

    def get_user_by_email(self, email):
        users = self.api_client.get_users()
        filtered = [u for u in users if u['email'] == email]
        if not filtered:
            raise UserNotFoundException(f'User with email "{email}" not found.')

        return filtered[0]

    def get_posts_by_user_email(self, email):
        user_id = self.get_user_by_email(email)['id']
        posts = self.api_client.get_posts(users_id=user_id)
        return posts
