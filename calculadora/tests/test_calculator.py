from unittest import TestCase
from src.utils import *


class TestCalculator(TestCase):
    def setUp(self) -> None:
        # Establece una configuracion por defecto
        self.vacio = ''
        self.error = 'ERROR'
        self.expressionRes = '475-25'  # 450
        self.expressionMul = '25*6'  # 150
        self.expressionDiv = '24/6'  # 4
        self.expressionSum = '10+9'  # 19
        self.expressionPot = '5**5'  # 3125
        self.expressionCompleja = '2*4-3*2'  # 2
        self.expressionErronea = '//8/-5+-++8'  # Error
        return super().setUp()

    def test_suma_10_mas_9(self):
        res = evaluate(self.expressionSum)
        self.assertEqual(19, int(res))

    def test_resta_475_menos_25(self):
        res = evaluate(self.expressionRes)
        self.assertEqual(450, int(res))

    def test_divide_24_para_6(self):
        res = evaluate(self.expressionDiv)
        self.assertEqual(4.0, float(res))

    def test_multiplica_25_por_6(self):
        res = evaluate(self.expressionMul)
        self.assertEqual(150, int(res))

    def test_eleva_5_a_5(self):
        res = evaluate(self.expressionPot)
        self.assertEqual(3125, int(res))

    def test_expression_erronea(self):
        res = evaluate(self.expressionErronea)
        self.assertEqual(self.error, res)

    def test_elimina_ultimo_valor(self):
        res = deleteToken('458-125')
        self.assertEqual('458-12', res)

    def test_limpia_toda_la_expresion(self):
        res = deleteAllTokens()
        self.assertEqual(self.vacio, res)
