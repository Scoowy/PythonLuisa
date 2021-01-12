from PyQt5.QtCore import QObject, pyqtSignal


class MainModel(QObject):
    """
    Model para la vista principal
    """
    rangeValueChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self._rangeValue = 0

    @property
    def rangeValue(self) -> int:
        """
        rangeValue property.
        """
        return self._rangeValue

    @rangeValue.setter
    def rangeValue(self, value):
        self._rangeValue = value
        self.rangeValueChanged.emit(self._rangeValue)
