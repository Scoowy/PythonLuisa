from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from src.view_ui import Ui_MainWindow


class ConversorView(QMainWindow):

    def __init__(self, model, controller) -> None:
        super().__init__()
        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)

        self.connectWithController()
        self.connectWithModel()

    def connectWithController(self):
        """
        Metodo en el cual se conectan todos los eventos de la interfaz con sus respectivos controladores
        """
        pass

    def connectWithModel(self):
        """
        Metodo en el cual se conectan todos los cambios del modelo con la interfaz
        """
        pass
