import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_get_missing_key(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k3"), None)

    def test_get_existing_key(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get("k1"), "val1")
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_get_key_removed_from_cache(self):
        self.test_get_existing_key()
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get("k1"), None)
        self.assertEqual(self.cache.get("k3"), "val3")
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_set_change(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "value1")
        self.cache.set("k2", "value2")
        self.assertEqual(self.cache.get("k1"), "value1")
        self.assertEqual(self.cache.get("k2"), "value2")

    def test_set_change_and_offset_in_cache(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "value1")
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get("k1"), "value1")
        self.assertEqual(self.cache.get("k3"), "val3")
        self.assertEqual(self.cache.get("k2"), None)
