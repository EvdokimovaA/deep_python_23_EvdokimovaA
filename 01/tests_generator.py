import io
import unittest
from generator import generator


class TestGenerator(unittest.TestCase):
    def test_found(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = generator(file, ['роза'])
        self.assertEqual(list(gen), ['а Роза упала на лапу Азора'])

    def test_found_several(self):
        file = io.StringIO('а Роза упала на лапу Азора\nалая РОЗА\nАзор')
        gen = generator(file, ['РоЗа'])
        self.assertEqual(list(gen), ['а Роза упала на лапу Азора\n',
                                     'алая РОЗА\n'])

    def test_not_found(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = generator(file, ['роз'])
        self.assertEqual(list(gen), [])

    def test_empty_file(self):
        file = io.StringIO('')
        gen = generator(file, ['роза'])
        self.assertEqual(list(gen), [])

    def test_empty_words_list(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = generator(file, [])
        self.assertEqual(list(gen), [])

    def test_words_list_with_empty_string(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = generator(file, [''])
        self.assertEqual(list(gen), [])

    def test_incorrect_file_descriptor(self):
        file = 23
        generator(file, ['роза'])
        self.assertRaises(TypeError, "Expected a different type of variable")

    def test_matching_multiple_filters_in_one_line(self):
        file = io.StringIO('роза и лапа\nроза алая')
        gen = generator(file, ['роза', 'лапа'])
        self.assertEqual(list(gen), ['роза и лапа\n',
                                     'роза алая'])

    def test_match_filter_and_file_string(self):
        file = io.StringIO('роза и лапа\nалая')
        gen = generator(file, ['алая'])
        self.assertEqual(list(gen), ['алая'])
