import time
import unittest
from time import sleep
from decorator import mean


class TestsDecorator(unittest.TestCase):
    def setUp(self):
        self.time_sleep = 0.1
        self.calls = 5

    def test_decorator_mean_calculation(self):
        @mean(self.calls)
        def to_be_decorated():
            sleep(self.time_sleep)

        list_results = []
        for i in range(100):
            list_results.append(round(to_be_decorated(), 1))

        check = all(i == self.time_sleep for i in list_results)
        self.assertTrue(check)

    def test_incorrect_type_k(self):
        @mean(str(self.calls))
        def to_be_decorated():
            time.sleep(self.time_sleep)

        self.assertRaises(TypeError, to_be_decorated)

    def test_incorrect_k_value(self):
        @mean(-self.calls)
        def to_be_decorated():
            time.sleep(self.time_sleep)

        self.assertRaises(ValueError, to_be_decorated)
