from PyQt5.QtCore import QObject
from src.model.M_MainWindow import MainModel


class MainController(QObject):
    """
    Controlador de la vista pricipal
    """

    def __init__(self, model: MainModel):
        """
        Constructor de clase
        """
        super().__init__()

        self._model = model
