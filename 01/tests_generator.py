import unittest
import io
from generator import search_matches, generator


class TestSearchMatches(unittest.TestCase):
    def test_search_matches(self):
        line = "this is a test line"
        list_search = ["test", "line"]
        self.assertEqual(search_matches(line, list_search), True)


class TestGenerator(unittest.TestCase):
    def setUp(self):
        text_file = "this is a test file\nwith some words\nfor searching\n"
        self.test_file = io.StringIO(text_file)
        self.file_descriptor = open("text", "r", encoding="UTF-8")
        self.file_descriptor.close()
        self.file = "text"

    def test_generator_with_file_name(self):
        list_search = ["генератор", "файла", "слов"]
        result = list(generator(self.file, list_search))
        self.assertEqual(len(result), 6)

    def test_generator_with_file_descriptor(self):
        list_search = ["слов"]
        expected_result = \
            ['набор слов разделенных пробелами знаков препинания нет\n',
             'или файловый объект и список слов для поиска\n',
             'где встретилось хотя бы одно из слов для поиска\n']
        result = list(generator(self.file_descriptor.name, list_search))
        self.assertEqual(len(result), 3)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
