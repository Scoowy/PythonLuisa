from factorial import factorial
from unittest import TestCase


class TestFacto(TestCase):
    def setUp(self) -> None:
        self.numero = 6
        self.resultadoDe6 = 720
        return super().setUp()

    def test_factorial_de_6(self):
        res = factorial(self.numero)
        self.assertEqual(self.resultadoDe6, res, "EL resultado es incorrecto")

    def test_factorial_de_8(self):
        res = factorial(8)
        self.assertEqual(40320, res, "EL resultado es incorrecto")
