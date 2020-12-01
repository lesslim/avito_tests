import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    """Класс для тестирования fit_transform из one_hot_encoder.py"""

    def test_list(self):
        """Аргумент функции - список."""
        actual = fit_transform(["a", "b", "c"])
        expected = [
            ("a", [0, 0, 1]),
            ("b", [0, 1, 0]),
            ("c", [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_str(self):
        """Аргумент функции - строки."""
        actual = fit_transform("a", "b", "c")
        expected = [
            ("a", [0, 0, 1]),
            ("b", [0, 1, 0]),
            ("c", [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """Аргумент функции - пустой список."""
        self.assertEqual(fit_transform([]), [])

    def test_bad_input(self):
        """Аргумент функции невалидный - числа."""
        with self.assertRaises(TypeError):
            fit_transform(1, 2)

    def test_empty_input(self):
        """Функция без аргумента."""
        self.assertRaises(TypeError, fit_transform)

    def test_not_in(self):
        """В результате нет значения."""
        self.assertNotIn((1, [0, 2]), fit_transform([1, 2, 1]))
