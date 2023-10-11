import unittest
from custom_meta import CustomClass


class TestCustomClass(unittest.TestCase):
    def test_default_class_attrs_with_custom_prefix(self):
        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertTrue(hasattr(CustomClass, 'custom_line'))

    def test_default_class_attrs_without_custom_prefix(self):
        self.assertFalse(hasattr(CustomClass, 'x'))
        self.assertFalse(hasattr(CustomClass, 'line'))

    def test_magic_methods(self):
        new_class_instance = CustomClass()
        self.assertTrue(hasattr(new_class_instance, '__dict__'))
        self.assertTrue(hasattr(new_class_instance, '__init__'))
        self.assertTrue(hasattr(new_class_instance, '__setattr__'))

        self.assertFalse(hasattr(new_class_instance, 'custom___dict__'))
        self.assertFalse(hasattr(new_class_instance, 'custom___init__'))
        self.assertFalse(hasattr(new_class_instance, 'custom___setattr__'))

    def test_custom_class_attrs_value(self):
        new_class_instance = CustomClass(55)
        self.assertEqual(new_class_instance.custom_x, 50)
        self.assertEqual(new_class_instance.custom_val, 55)

    def test_method_line(self):
        new_class_instance = CustomClass()
        self.assertTrue(hasattr(new_class_instance, 'custom_line'))
        self.assertFalse(hasattr(new_class_instance, 'line'))
        self.assertEqual(new_class_instance.custom_line(), 100)

    def test_method__str__(self):
        new_class_instance = CustomClass()
        self.assertTrue(hasattr(new_class_instance, '__str__'))
        self.assertFalse(hasattr(new_class_instance, 'custom___str__'))
        self.assertEqual(str(new_class_instance), 'Custom_by_metaclass')

    def test_custom_class_dynamic_attrs_val(self):
        new_class_instance = CustomClass()
        new_class_instance.new_attr = 123
        self.assertTrue(hasattr(new_class_instance, 'custom_new_attr'))
        self.assertFalse(hasattr(new_class_instance, 'new_attr'))
        self.assertEqual(new_class_instance.custom_new_attr, 123)
