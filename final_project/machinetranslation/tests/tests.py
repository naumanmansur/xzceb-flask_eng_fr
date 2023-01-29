import unittest
from translator import english_to_french, french_to_english
class test_english_to_french(unittest.Testcase):
    def test1(self):
        self.assertEqual(english_to_french(None),None)
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Bonjour'),'Hello')

class test_french_to_english(unittest.Testcase):
    def test1(self):
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')

unittest.main()
