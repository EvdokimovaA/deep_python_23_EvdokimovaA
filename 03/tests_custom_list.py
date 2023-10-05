import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.lst1 = CustomList([5, 1, 3, 7])
        self.lst2 = CustomList([1, 2, 7])
        self.lst3 = [2, 5]

    def test_add_list_equal_len(self):
        result = self.lst1 + [5, 1, 3, 7]
        self.assertEqual(result, CustomList([10, 2, 6, 14]))

        result = [5, 1, 3, 7] + self.lst1
        self.assertEqual(result, CustomList([10, 2, 6, 14]))

    def test_add_custom_list_equal_len(self):
        result = self.lst1 + CustomList([5, 1, 3, 7])
        self.assertEqual(result, CustomList([10, 2, 6, 14]))

        result = CustomList([5, 1, 3, 7]) + self.lst1
        self.assertEqual(result, CustomList([10, 2, 6, 14]))

    def test_add_custom_list_not_equal_len(self):
        result = self.lst1 + self.lst2
        self.assertEqual(result, CustomList([6, 3, 10, 7]))

    def test_add_list_not_equal_len(self):
        result = self.lst1 + self.lst3
        self.assertEqual(result, CustomList([7, 6, 3, 7]))

        result = self.lst3 + self.lst1
        self.assertEqual(result, CustomList([7, 6, 3, 7]))

    def test_sub_custom_list_not_equal_len(self):
        result = self.lst1 - self.lst2
        self.assertEqual(result, CustomList([4, -1, -4, 7]))

    def test_sub_list_not_equal_len(self):
        result = self.lst1 - self.lst3
        self.assertEqual(result, CustomList([3, -4, 3, 7]))

        result = self.lst3 - self.lst1
        self.assertEqual(result, CustomList([-3, 4, -3, -7]))

    def test_eq_nq_custom_lists(self):
        self.assertTrue(self.lst1 == self.lst1)
        self.assertFalse(self.lst1 != self.lst1)

    def test_lt_gt_custom_lists(self):
        self.assertTrue(self.lst1 > self.lst2)
        self.assertFalse(self.lst1 < self.lst2)

    def test_le_ge_custom_lists(self):
        self.assertTrue(self.lst1 >= self.lst1)
        self.assertTrue(self.lst1 <= self.lst1)

    def test_check_correct_type(self):
        self.assertRaises(TypeError, CustomList._check_correct_type, 5)
