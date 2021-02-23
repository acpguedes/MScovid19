import unittest
from unittest.mock import patch, MagicMock
from mscovid.fetch import CovidGetData


def request_ok():
    return MagicMock(status_code=200)


def request_fail():
    return MagicMock(status_code=500)


class MScovid19Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
