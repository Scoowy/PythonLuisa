from PyQt5.QtCore import QObject, pyqtSignal


class ConversorModel(QObject):
    """
    Modelo del conversor
    """

    resultChanged = pyqtSignal(str)
    valueInChanged = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self._result = 0
        self._valueIn = 0

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

    @property
    def valueIn(self) -> int:
        """
        valueIn property.
        """
        return self._valueIn

    @valueIn.setter
    def valueIn(self, value):
        self._valueIn = value

    def metersToCentimeters(self):
        pass

    def celciusToFahrenheit(self):
        pass
