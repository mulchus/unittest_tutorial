import random
import math
import unittest
from unittest.mock import patch


def get_random_int():
    return random.randint(1, 100)


class TestFunction(unittest.TestCase):
    @patch("random.randint")
    def test_get_random_int(self, mock_random_int):
        mock_random_int.return_value = 10
        assert get_random_int() == 10


def test_get_random_int():
    with patch("random.randint", return_value=5):
        assert get_random_int() == 5


def get_log_two(a: int) -> float:
    return math.log2(a)


class TestLogTwo(unittest.TestCase):
    @patch("math.log2")
    def test_add_two_numbers(self, mock_get_log_two):
        mock_get_log_two.return_value = 0
        assert get_log_two(5) == 0


def get_sum(a: int, b: int) -> int:
    return a + b


class TestAddTwoNumbers(unittest.TestCase):
    @patch("sample.get_sum")
    def test_get_sum(self, mock_get_sum):
        mock_get_sum.return_value = 100
        assert get_sum(5, 6) == 100
