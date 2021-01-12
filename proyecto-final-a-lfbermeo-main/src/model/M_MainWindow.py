from PyQt5.QtCore import QObject, pyqtSignal


class MainModel(QObject):
    """
    Model para la vista principal
    """
    component_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self._component_selected = 0
