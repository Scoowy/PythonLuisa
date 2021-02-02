from unittest import TestCase
from src.model import CalculatorModel


class TestCalculator(TestCase):
    def setUp(self) -> None:
        # Establece una configuracion por defecto
        self.calculadora = CalculatorModel()
        self.vacio = ''
        self.error = 'ERROR'
        self.expressionAntesBorrar = '458-125'
        self.expressionDespuesBorrar = '458-12'
        self.expressionRes = '475-25'  # 450
        self.expressionMul = '25*6'  # 150
        self.expressionDiv = '24/6'  # 4
        self.expressionSum = '10+9'  # 19
        self.expressionPot = '5**5'  # 3125
        self.expressionCompleja = '2*4-3*2'  # 2
        self.expressionErronea = '//8/-5+-++8'  # Error
        return super().setUp()

    def test_suma_10_mas_9(self):
        self.calculadora.expression = self.expressionSum
        self.calculadora.evaluateExpression()
        self.assertEqual(19, int(self.calculadora.expression))

    def test_resta_475_menos_25(self):
        self.calculadora.expression = self.expressionRes
        self.calculadora.evaluateExpression()
        self.assertEqual(450, int(self.calculadora.expression))

    def test_divide_24_para_6(self):
        self.calculadora.expression = self.expressionDiv
        self.calculadora.evaluateExpression()
        self.assertEqual(4.0, float(self.calculadora.expression))

    def test_multiplica_25_por_6(self):
        self.calculadora.expression = self.expressionMul
        self.calculadora.evaluateExpression()
        self.assertEqual(150, int(self.calculadora.expression))

    def test_eleva_5_a_5(self):
        self.calculadora.expression = self.expressionPot
        self.calculadora.evaluateExpression()
        self.assertEqual(3125, int(self.calculadora.expression))

    def test_expression_erronea(self):
        self.calculadora.expression = self.expressionErronea
        self.calculadora.evaluateExpression()
        self.assertEqual(self.error, self.calculadora.expression)

    def test_elimina_ultimo_valor(self):
        self.calculadora.expression = self.expressionAntesBorrar
        self.calculadora.deleteLastToken()
        self.assertEqual(self.expressionDespuesBorrar,
                         self.calculadora.expression)

    def test_limpia_toda_la_expresion(self):
        self.calculadora.expression = self.expressionAntesBorrar
        self.calculadora.deleteAllTokens()
        self.assertEqual(self.vacio, self.calculadora.expression)
