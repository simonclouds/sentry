from __future__ import absolute_import

from sentry.testutils import TestCase
from sentry.utils.safe import trim

a_very_long_string = 'a' * 1024


class TrimTest(TestCase):
    def test_simple_string(self):
        assert trim(a_very_long_string) == a_very_long_string[:509] + '...'

    def test_list_of_strings(self):
        assert trim([a_very_long_string, a_very_long_string]) == [
            a_very_long_string[:507] + '...',
        ]
