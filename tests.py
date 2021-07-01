import unittest

from translator import english_to_french, english_to_german


class TestEnglishToFrench(unittest.TestCase):
    def test_translate1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_translate2(self):
        self.assertEqual(english_to_french("Hi"), "Salut")

    def test_null(self):
        self.assertEqual(english_to_french(None), "No text provided!")


class TestEnglishToGerman(unittest.TestCase):
    def test_translate1(self):
        self.assertEqual(english_to_german("Thank you"), "Danke.")

    def test_translate2(self):
        self.assertEqual(english_to_german("Hello"), "Hallo")

    def test_null(self):
        self.assertEqual(english_to_german(None), "No text provided!")
