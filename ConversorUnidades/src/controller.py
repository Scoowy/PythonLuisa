from PyQt5.QtCore import QObject, pyqtSlot

from src.model import ConversorModel


class ConversorController(QObject):
    """
    Controlador de la vista conversor
    """

    def __init__(self, model: ConversorModel) -> None:
        super().__init__()

        self._model = model

    @pyqtSlot(str)
    def convertDistance(self, value):
        print("m -> cm")

    @pyqtSlot(str)
    def convertTemperature(self, value):
        print("c -> f")
