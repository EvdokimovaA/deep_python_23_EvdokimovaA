import contextlib
import io
import sys
import time
import unittest
from time import sleep
from decorator import mean


class TestsDecorator(unittest.TestCase):
    def setUp(self):
        self.time_sleep = 0.1
        self.calls = 5

    def test_return_decorated_func(self):
        @mean(self.calls)
        def to_be_decorated():
            sleep(self.time_sleep)
            return 3

        result = to_be_decorated()
        self.assertEqual(result, 3)

    def test_average_execution_time_many_calls(self):
        def to_be_decorated():
            sleep(self.time_sleep)
            return 3

        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        for i in range(10):
            to_be_decorated()

        lst = sys.stdout.getvalue().split()
        list_results = [round(float(i), 1) for i in lst]
        check = all(i == self.time_sleep for i in list_results)
        self.assertTrue(check)
        sys.stdout = original_stdout

    def test_print_work_time_one_call(self):
        @mean(self.calls)
        def to_be_decorated():
            sleep(self.time_sleep)

        with contextlib.redirect_stdout(io.StringIO()) as captured_output:
            to_be_decorated()

        actual_output = round(float(captured_output.getvalue()), 1)
        self.assertEqual(actual_output, self.time_sleep)

    def test_incorrect_type_k(self):
        def to_be_decorated():
            time.sleep(self.time_sleep)

        with self.assertRaises(TypeError):
            mean(str(self.calls))(to_be_decorated)

    def test_incorrect_k_value(self):
        def to_be_decorated():
            time.sleep(self.time_sleep)

        with self.assertRaises(ValueError):
            mean(-self.calls)(to_be_decorated)
