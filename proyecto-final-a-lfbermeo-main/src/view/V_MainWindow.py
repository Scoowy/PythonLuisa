from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from src.controller.C_MainWindow import MainController
from src.model.M_MainWindow import MainModel

from src.view.MainWindow_ui import Ui_MainWindow


class MainView(QMainWindow):
    """
    Watcher main view
    """

    def __init__(self, model: MainModel, controller: MainController):
        """
        Constructor
        """
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
