import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.lst1 = CustomList([5, 1, 3, 7])
        self.lst2 = CustomList([1, 2, 7])
        self.lst3 = [2, 5]

    def test_add_list_equal_len_right(self):
        result = self.lst1 + [5, 1, 3, 7]
        self.assertEqual(list(result), [10, 2, 6, 14])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_add_list_equal_len_left(self):
        result = [5, 1, 3, 7] + self.lst1
        self.assertEqual(list(result), [10, 2, 6, 14])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_add_custom_list_equal_len_right(self):
        result = self.lst1 + CustomList([5, 1, 3, 7])
        self.assertEqual(list(result), [10, 2, 6, 14])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_add_custom_list_equal_len_left(self):
        result = CustomList([5, 1, 3, 7]) + self.lst1
        self.assertEqual(list(result), [10, 2, 6, 14])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_add_custom_list_not_equal_len_right(self):
        result = self.lst1 + self.lst2
        self.assertEqual(list(result), [6, 3, 10, 7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_add_custom_list_not_equal_len_left(self):
        result = self.lst2 + self.lst1
        self.assertEqual(list(result), [6, 3, 10, 7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_add_list_not_equal_len_right(self):
        result = self.lst1 + self.lst3
        self.assertEqual(list(result), [7, 6, 3, 7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_add_list_not_equal_len_left(self):
        result = self.lst3 + self.lst1
        self.assertEqual(list(result), [7, 6, 3, 7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_sub_custom_list_not_equal_len_right(self):
        result = self.lst1 - self.lst2
        self.assertEqual(list(result), [4, -1, -4, 7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_sub_custom_list_not_equal_len_left(self):
        result = self.lst2 - self.lst1
        self.assertEqual(list(result), [-4, 1, 4, -7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_sub_list_not_equal_len_right(self):
        result = self.lst1 - self.lst3
        self.assertEqual(list(result), [3, -4, 3, 7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_sub_list_not_equal_len_left(self):
        result = self.lst3 - self.lst1
        self.assertEqual(list(result), [-3, 4, -3, -7])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_sub_list_equal_len_right(self):
        result = self.lst1 - [5, 1, 3, 7]
        self.assertEqual(list(result), [0, 0, 0, 0])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_sub_list_equal_len_left(self):
        result = [5, 1, 3, 7] - self.lst1
        self.assertEqual(list(result), [0, 0, 0, 0])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_sub_custom_list_equal_len_right(self):
        result = self.lst1 - self.lst1
        self.assertEqual(list(result), [0, 0, 0, 0])
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_sub_custom_list_equal_len_left(self):
        result = self.lst2 - self.lst2
        self.assertEqual(list(result), [0, 0, 0])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_eq_nq_custom_lists(self):
        self.assertTrue(self.lst1 == self.lst1)
        self.assertFalse(self.lst1 == self.lst2)
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_lt_gt_custom_lists(self):
        self.assertTrue(self.lst1 > self.lst2)
        self.assertFalse(self.lst1 < self.lst2)
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
        self.assertEqual(list(self.lst2), [1, 2, 7])

    def test_le_ge_custom_lists(self):
        self.assertTrue(self.lst1 >= self.lst1)
        self.assertTrue(self.lst1 <= self.lst1)
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])

    def test_eq_lists_different_elements_and_same_sum(self):
        l1 = CustomList([1, 2, 3])
        l2 = CustomList([3, 2, 1])
        self.assertTrue(l1 == l2)
        self.assertEqual(list(l1), [1, 2, 3])
        self.assertEqual(list(l2), [3, 2, 1])

    def test_check_correct_type(self):
        self.assertRaises(TypeError, CustomList._check_correct_type, 5)

    def test__str__(self):
        message = f'[5, 1, 3, 7] Сумма: {sum(self.lst1)}'
        self.assertEqual(str(self.lst1), message)
        self.assertEqual(list(self.lst1), [5, 1, 3, 7])
