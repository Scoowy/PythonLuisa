from src.problem1 import *
import unittest

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.cadenaesperada =  'Este archivo tiene algunos caracteres especiales'
    def test_sub(self):
        self.assertEqual(remover_puntuacion("mensaje.txt"), self.cadenaesperada)