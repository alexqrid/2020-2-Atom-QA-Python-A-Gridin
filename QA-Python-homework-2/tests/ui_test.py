import os
import pytest
from tests.base import BaseCase


class Test(BaseCase):

    # @pytest.mark.skip(reason="passed")
    @pytest.mark.UI
    def test_positive_auth(self, credentials):
        self.main_page.login(credentials)
        assert self.main_page.is_authenticated()

    # @pytest.mark.skip(reason="passed")
    @pytest.mark.UI
    def test_negative_auth(self):
        self.main_page.login({"email": "test", "password": "21321321"})
        assert not self.main_page.is_authenticated(timeout=.1)

    # @pytest.mark.skip(reason="passed")
    @pytest.mark.UI
    def test_campaign_creation(self, authenticate, unique):
        self.dashboard = authenticate
        self.dashboard.go_to_campaign()
        image_path = os.path.join(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))),
            "static/campaign.png")
        print(image_path)
        assert self.campaign.create_campaign(title=unique,
                                             image_path=image_path)

    # @pytest.mark.skip("passed")
    @pytest.mark.UI
    def test_segment_creation(self, authenticate, unique):
        self.dashboard = authenticate
        self.dashboard.go_to_audience()
        assert self.audience.create_audience(title=unique)

    # @pytest.mark.skip(reason="passed")
    @pytest.mark.UI
    def test_segment_remove(self, authenticate, unique):
        self.dashboard = authenticate
        self.dashboard.go_to_audience()
        assert self.audience.delete_audience(title=unique)
