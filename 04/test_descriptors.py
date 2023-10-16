import unittest
from descriptors import Human


class TestDescriptors(unittest.TestCase):
    def test_correct_data_types(self):
        human = Human("Valera", 30, 80.3)
        self.assertIsInstance(human.name, str)
        self.assertIsInstance(human.age, int)
        self.assertIsInstance(human.weight, (int, float))

    def test_correct_data_values(self):
        human = Human("Valera", 30, 80.3)
        self.assertEqual(human.name, "Valera")
        self.assertEqual(human.age, 30)
        self.assertEqual(human.weight, 80.3)

    def test_incorrect_name_type(self):
        with self.assertRaises(ValueError):
            Human(11, 30, 80.3)

    def test_incorrect_age_type(self):
        with self.assertRaises(ValueError):
            Human("Valera", 12.2, 80.3)

    def test_incorrect_weight_type(self):
        with self.assertRaises(ValueError):
            Human("Valera", 30, "10")

    def test_incorrect_age_val(self):
        with self.assertRaises(ValueError):
            Human("Valera", 500, 80.3)

    def test_incorrect_weight_val(self):
        with self.assertRaises(ValueError):
            Human("Valera", 30, -1)

    def test_correct_change_name(self):
        human = Human("Valera", 30, 80.3)
        human.name = "Jon"
        self.assertEqual(human.name, "Jon")
        self.assertEqual(human.age, 30)
        self.assertEqual(human.weight, 80.3)

    def test_correct_change_age(self):
        human = Human("Valera", 30, 80.3)
        human.age = 20
        self.assertEqual(human.name, "Valera")
        self.assertEqual(human.age, 20)
        self.assertEqual(human.weight, 80.3)

    def test_correct_change_weight(self):
        human = Human("Valera", 30, 80.3)
        human.weight = 90
        self.assertEqual(human.name, "Valera")
        self.assertEqual(human.age, 30)
        self.assertEqual(human.weight, 90)

    def test_incorrect_change_name(self):
        human = Human("Valera", 30, 80.3)
        with self.assertRaises(ValueError):
            human.name = 11
        self.assertEqual(human.name, "Valera")
        self.assertEqual(human.age, 30)
        self.assertEqual(human.weight, 80.3)

    def test_incorrect_change_age(self):
        human = Human("Valera", 30, 80.3)
        with self.assertRaises(ValueError):
            human.age = 500
        self.assertEqual(human.name, "Valera")
        self.assertEqual(human.age, 30)
        self.assertEqual(human.weight, 80.3)

    def test_incorrect_change_weight(self):
        human = Human("Valera", 30, 80.3)
        with self.assertRaises(ValueError):
            human.weight = -1
        self.assertEqual(human.name, "Valera")
        self.assertEqual(human.age, 30)
        self.assertEqual(human.weight, 80.3)

    def test_several_instances_of_class_Human(self):
        human1 = Human("Valera", 30, 80.3)
        human2 = Human("Qwerty", 10, 35)
        self.assertEqual(human1.name, "Valera")
        self.assertEqual(human1.age, 30)
        self.assertEqual(human1.weight, 80.3)
        self.assertEqual(human2.name, "Qwerty")
        self.assertEqual(human2.age, 10)
        self.assertEqual(human2.weight, 35)

    def test_refer_to__get__via_class_name(self):
        Human("Valera", 30, 80.3)
        self.assertIsNone(Human.name)
        self.assertIsNone(Human.age)
        self.assertIsNone(Human.weight)
