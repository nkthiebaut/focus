import json
import pytest
from focus.api import app


class TestApi(object):
    """Test the API."""
    @pytest.fixture(scope='function')
    def sample_query(self):
        """Create a sample query with an acceptable format"""
        return '/job_title?offer=developer&cand=php%20engineer'

    def test_api(self, sample_query):
        """Run test API client and try a dummy query"""
        with app.test_client() as c:
            api_response = c.get(sample_query)
            out_data = json.loads(api_response.data)['data']
            assert isinstance(out_data, dict)
            assert float(out_data['score']) > 0.

