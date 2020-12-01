import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now
import urllib.request
import io


class TestWhatIsYearNow(unittest.TestCase):
    """Класс для тестирования what_is_year_now из what_is_year_now.py."""

    def test_year_now(self):
        """Проверка текущего года."""
        actual = what_is_year_now()
        expected = 2020
        self.assertEqual(actual, expected)

    def test_wrong_year(self):
        """Проверка на ошибку прошлого года."""
        actual = what_is_year_now()
        expected = 2019
        with self.assertRaises(AssertionError):
            self.assertEqual(actual, expected)

    def test_dash(self):
        """Проверка на дату в формате 'YYYY-MM-DD'."""
        dict_json = '{"currentDateTime": "2020-12-01"}'

        with patch.object(
            urllib.request, "urlopen", return_value=io.StringIO(dict_json)
        ):
            actual = what_is_year_now()
        expected = 2020
        self.assertEqual(actual, expected)

    def test_point(self):
        """Проверка на дату в формате  'DD.MM.YYYY'."""
        dict_json = '{"currentDateTime": "01.12.2020"}'

        with patch.object(
            urllib.request, "urlopen", return_value=io.StringIO(dict_json)
        ):
            actual = what_is_year_now()
        expected = 2020
        self.assertEqual(actual, expected)

    def test_wrong_sep(self):
        """Проверка на некорректный разделитель."""
        dict_json = '{"currentDateTime": "01:12:2020"}'

        with patch.object(
            urllib.request, "urlopen", return_value=io.StringIO(dict_json)
        ):
            with self.assertRaises(ValueError):
                what_is_year_now()

    def test_wrong_format(self):
        """Проверка на некорректный формат даты."""
        dict_json = '{"currentDateTime": "1.12.2020"}'

        with patch.object(
            urllib.request, "urlopen", return_value=io.StringIO(dict_json)
        ):
            with self.assertRaises(ValueError):
                what_is_year_now()

    def test_big_json(self):
        """Проверка на дату в формате  'DD.MM.YYYY'."""
        dict_json = (
            '{"$id":"1","currentDateTime":"2021-12-01T11:03Z","utcOffset":"00:00:00"}'
        )

        with patch.object(
            urllib.request, "urlopen", return_value=io.StringIO(dict_json)
        ):
            actual = what_is_year_now()
        expected = 2021
        self.assertEqual(actual, expected)
