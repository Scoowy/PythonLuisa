from src.problem2 import regex_ayuda
import unittest

class TestProblem2(unittest.TestCase):
    def setUp(self):
        pass

    def test_findall(self):
        self.assertEqual(regex_ayuda(r"\d\d\d-\d\d\d-\d\d\d\d",
                                     "Cell: 415-555-9999 Work: 212-555-0000"),
                         ['415-555-9999', '212-555-0000'])
        self.assertEqual(regex_ayuda(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)',
                                     "Cell: 415-555-9999 Work: 212-555-0000"),
                         [('415', '555', '9999'), ('212', '555', '0000')])
        self.assertEqual(regex_ayuda(r'[aeiouAEIOU]',
                                     'Robocop eats baby food. BABY FOOD.'),
                         ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O'])



