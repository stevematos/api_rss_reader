import unittest
from . import test_sql_app


class TestGraphql(unittest.TestCase):
    def test_feed(self):
        test_sql_app.test_feed()

    def test_register_and_login(self):
        test_sql_app.test_login()

    def test_subscribe_feed(self):
        test_sql_app.test_subscribe_feed()


if __name__ == '__main__':
    unittest.main()

