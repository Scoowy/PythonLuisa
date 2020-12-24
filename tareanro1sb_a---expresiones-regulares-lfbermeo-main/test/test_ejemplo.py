from src.ejemplo import *
import unittest

class TestEjemplo(unittest.TestCase):
    
    def test_ejemplo(self):
        self.assertEqual(obtener_palabras("ejemplo de cadena"), ['ejemplo', 'de', 'cadena'])