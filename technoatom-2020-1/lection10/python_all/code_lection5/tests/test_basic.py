import random

import pytest

from tests.base import BaseCase, UserNotFoundException


class TestApi(BaseCase):

    def test_simple(self):
        email = "Rey.Padberg@karina.biz"
        user_posts = self.get_posts_by_user_email(email)
        assert len(user_posts) == 100

    def test_negative(self):
        email = "321321321@321321.3213213.3213213"
        with pytest.raises(UserNotFoundException):
            self.get_posts_by_user_email(email)

    def test_create_post(self):
        result = self.api_client.post_posts(title='test', body='test', user_id=1)
        assert result['id'] == 101

    def test_create_post_negative(self):
        result = self.api_client.post_posts_failed(title='test', body='test', user_id=1)
        assert result == {}

    @pytest.fixture(scope='function')
    def new_post(self, api_client):
        user_id = random.randint(1, 1000)
        title = '321312312'
        body = '321312321'

        post = api_client.post_posts(user_id=user_id, title=title, body=body)
        yield post
        api_client.delete_posts(post['id'])

    def test_delete_post(self, new_post):
        assert new_post['id'] == 101
        print(new_post)
