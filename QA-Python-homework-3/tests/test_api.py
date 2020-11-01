from tests.base import BaseCase
import pytest
import uuid


class TestAPI(BaseCase):
    # @pytest.mark.skip(reason="passed")
    @pytest.mark.API
    def test_segment_creation(self, unique):
        id = self.client.create_segment(name=unique)
        assert self.client.exists(id)

    # @pytest.mark.skip(reason="passed")
    @pytest.mark.API
    def test_segment_remove(self, unique):
        segment_id = self.client.create_segment(name=unique)
        assert self.client.exists(segment_id)
        assert self.client.segment_remove(segment_id=segment_id)
