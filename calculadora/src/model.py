from PyQt5.QtCore import QObject, pyqtSignal


class CalculatorModel(QObject):
    """
    Modelo de la vista calculator
    """

    expressionChanged = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self._expression = ''

    @property
    def expression(self) -> str:
        """
        resultValue property.
        """
        return self._expression

    @expression.setter
    def expression(self, value):
        self._expression = value
        self.expressionChanged.emit(self._expression)

    def addToken(self, token):
        """
        Metodo que recibe una expresion y aniade un nuevo caracter
        """
        # Si la expresion anterior es ERROR se limpia y se aniade el nuevo caracter
        if self.expression == 'ERROR':
            self.expression = ''

        self.expression = self.expression + token

    def deleteLastToken(self):
        """
        Metodo que recibe una expresion y elimina el ultimo caracter
        """
        self.expression = self.expression[:-1]

    def deleteAllTokens(self):
        """
        Metodo que devuelve un string vacio representando que la 
        expresion a sido limpiada completametne
        """
        self.expression = ''

    def evaluateExpression(self):
        """
        Metodo que intenta evaluar la expresion.
        Si esta esta vacia se devulve vacio.
        Si contiene una expresion valida se evalua y devuelve el resultado en string.
        Si contiene una expresion no valida se devuelve el resultado 'ERROR'
        """
        if self.expression != '':
            try:
                res = eval(self.expression)
                self.expression = str(res)
            except:
                self.expression = 'ERROR'
        else:
            self.expression = ''
