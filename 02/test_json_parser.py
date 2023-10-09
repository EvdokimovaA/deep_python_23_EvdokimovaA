import sys
import unittest
from unittest.mock import Mock
from io import StringIO

from json_parser import parse_json, keyword_callback_func


class TestParser(unittest.TestCase):
    def setUp(self):
        self.input_json = '{"key1": "Word1 Word2 word2", "key2": "word2 word3"}'
        self.required_fields = ["key1", "key2"]
        self.keywords = ["word2"]

    def test_invalid_type_json_str(self):
        json_str = 23
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        parse_json(json_str, keyword_callback_func, self.required_fields, self.keywords)
        self.assertIn("Некорректный тип json строки", sys.stdout.getvalue())
        sys.stdout = original_stdout

    def test_invalid_json_str(self):
        invalid_json_str = '{"key": "value"'
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        parse_json(invalid_json_str, keyword_callback_func, self.required_fields, self.keywords)
        self.assertIn("Некорректный формат json строки", sys.stdout.getvalue())
        sys.stdout = original_stdout

    def test_empty_keywords(self):
        self.assertIsNone(parse_json(self.input_json, keyword_callback_func, self.required_fields))

    def test_empty_required_fields(self):
        self.assertIsNone(parse_json(self.input_json, keyword_callback_func, None, self.keywords))

    def test_parse_json_several_matches(self):
        keyword_callback_mock = Mock()
        result = parse_json(self.input_json, keyword_callback_mock, self.required_fields, self.keywords)

        self.assertEqual(keyword_callback_mock.call_count, 3)
        self.assertEqual(keyword_callback_mock.call_args[0], ('key2', 'word2'))
        self.assertEqual(result, '{"key1": "Word1 Word2 word2", "key2": "word2 word3"}')

    def test_parse_json_not_matches(self):
        keyword_callback_mock = Mock()
        result = parse_json(self.input_json, keyword_callback_mock, ["Key1"], self.keywords)

        self.assertEqual(keyword_callback_mock.call_count, 0)
        self.assertEqual(result, '{"key1": "Word1 Word2 word2", "key2": "word2 word3"}')
