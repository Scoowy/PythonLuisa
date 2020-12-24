from src.problem3 import *
import unittest

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.cadena = 'El profesor para CSCI0000 es ejemplo1@utpl.edu.ec y el número al que puede contactarlo es (401) 000-000 a partir de las 11:00.'

    def test_correos(self):
        self.assertEqual(obtenerCorreos(self.cadena), ['ejemplo1@utpl.edu.ec'])

    def test_horas(self):
        self.assertEqual(obtenerHoras(self.cadena), ['11:00'])

    def test_cursos(self):
        self.assertEqual(obtenerCursos(self.cadena), ['CSCI0000'])

if __name__ == '__main__':
    unittest.main()