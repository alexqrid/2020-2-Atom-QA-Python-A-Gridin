import pytest

from api.technoatom_client import TechnoatomClient


class TestTechnoatom:

    @pytest.fixture(scope='function')
    def api_client(self):
        user = 'i.kirillov'
        password = open('/tmp/password').read().strip()

        return TechnoatomClient(user, password)

    @pytest.fixture(scope='function')
    def new_post(self, api_client):
        title = 'TEXT'
        text = 'TEXTTEXTTEXT'

        post = api_client.post_topic(title=title, text=text, publish=True)
        post_id = post['redirect_url'].strip('/').split('/')[-1]
        yield title, text
        api_client.delete_topic(post_id)

    def test_create_post(self, api_client, new_post):
        topic_title, topic_text = new_post

        posts = api_client.get_feed(feed_type='all')
        assert posts['items'][0]['object']['title'] == topic_title
        assert posts['items'][0]['object']['text'] == topic_text
