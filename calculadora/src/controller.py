from PyQt5.QtCore import QObject, pyqtSlot

from src.model import CalculatorModel


class CalculatorController(QObject):
    """
    Controlador de la vista calculator
    """

    def __init__(self, model: CalculatorModel) -> None:
        super().__init__()

        self._model = model

    @pyqtSlot(bool)
    def resolve(self, value):
        """
        Controlador que escucha el evento del boton "="
        """
        self._model.evaluateOperation()

    @pyqtSlot(str)
    def addToken(self, value):
        """
        Contorlador que escucha los eventos de los botones "0"..."9", "/", "*", "-", "+" y "."
        """
        self._model.addToken(value)

    @pyqtSlot(bool)
    def clear(self, value):
        """
        Controlador que escucha el evento del boton "<x"
        """
        self._model.deleteLastToken()

    @pyqtSlot(bool)
    def clearAll(self, value):
        """
        Controlador que escucha el evento del boton "AC"
        """
        self._model.deleteAllTokens()
