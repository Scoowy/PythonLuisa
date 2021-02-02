from PyQt5.QtCore import QObject, pyqtSignal


class ConversorModel(QObject):
    """
    Modelo del conversor
    """

    resultChanged = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self._result = 0

    @property
    def result(self) -> int:
        """
        result property.
        """
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
        self.valueInChanged.emit(self._result)

    def metersToCentimeters(self):
        pass

    def celciusToFahrenheit(self):
        pass
