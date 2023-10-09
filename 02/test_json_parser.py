import sys
import unittest
from unittest import mock
from io import StringIO
from unittest.mock import call

from json_parser import parse_json, keyword_callback_func


class TestParser(unittest.TestCase):
    def setUp(self):
        self.input_json = '{"key1": "Word1 Word2 word2 word4", "key2": "word2 word3 word3"}'
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

    def test_empty_keyword_callback(self):
        self.assertIsNone(parse_json(self.input_json, None, self.required_fields, self.keywords))

    def test_keyword_not_in_any_required_fields(self):
        with mock.patch('json_parser.keyword_callback_func') as mock_model:
            parse_json(self.input_json, mock_model, self.required_fields, ["word5"])
            mock_model.assert_not_called()
            parse_json(self.input_json, mock_model, self.required_fields, ["word6"])
            mock_model.assert_not_called()

    def test_search_keywords_case_insensitive(self):
        with mock.patch('json_parser.keyword_callback_func') as mock_model:
            parse_json(self.input_json, mock_model, self.required_fields, ["WoRd3"])
            self.assertEqual(mock_model.call_args[0], ('key2', 'word3'))

    def test_matching_several_keywords_in_one_line(self):
        with mock.patch('json_parser.keyword_callback_func') as mock_model:
            parse_json(self.input_json, mock_model, self.required_fields, ["word3"])
            self.assertEqual(mock_model.call_args_list, [call('key2', 'word3'), call('key2', 'word3')])

    def test_with_several_required_fields_and_keywords_found(self):
        expected_result = [call('key1', 'word2'), call('key1', 'word2'), call('key1', 'word4'), call('key2', 'word2')]
        with mock.patch('json_parser.keyword_callback_func') as mock_model:
            parse_json(self.input_json, mock_model, self.required_fields, ["word2", "word4"])
            self.assertEqual(mock_model.call_args_list, expected_result)
