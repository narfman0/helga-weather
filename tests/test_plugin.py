import json
import sys
from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    from mock import mock
sys.modules['helga.plugins'] = mock.Mock()


from helga_weather.plugin import extract_weather


PAYLOAD = {
    'main': {
        'temp': 3
    },
    'weather': [{
        'description': 'windy'
    }],
}


class TestResults(TestCase):
    def test_response_simple(self):
        temp_f, conditions = extract_weather(PAYLOAD)
        self.assertEqual(3, temp_f)
