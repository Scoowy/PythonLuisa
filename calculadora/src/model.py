from PyQt5.QtCore import QObject, pyqtSignal

from src.utils import appendToken, evaluate, deleteToken, deleteAllTokens


class CalculatorModel(QObject):
    """
    Modelo de la vista calculator
    """

    resultValueChanged = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self._resultValue = ''

    @property
    def resultValue(self) -> str:
        """
        resultValue property.
        """
        return self._resultValue

    @resultValue.setter
    def resultValue(self, value):
        self._resultValue = value
        self.resultValueChanged.emit(self._resultValue)

    def addToken(self, token):
        # print(f"Add token: {token}")
        self.resultValue = appendToken(self.resultValue, token)

    def deleteLastToken(self):
        self.resultValue = deleteToken(self.resultValue)

    def deleteAllTokens(self):
        self.resultValue = deleteAllTokens()

    def evaluateOperation(self):
        self.resultValue = evaluate(self.resultValue)
