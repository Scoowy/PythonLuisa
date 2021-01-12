from PyQt5.QtWidgets import QMainWindow, QRadioButton
from PyQt5.QtCore import pyqtSlot
from src.controller.C_MainWindow import MainController
from src.model.M_MainWindow import MainModel

from src.view.MainWindow_ui import Ui_MainWindow
from src.utils.enums import DataOptions, TypeOptions


class MainView(QMainWindow):
    """
    Clase que represnta la interfaz grafica (UI) de la aplicacion
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

        self.initializeValues()
        self.connectWithControllers()

    def initializeValues(self):
        """
        Metodo en el cual se inicializan algunos valores
        """
        self._ui.listCountries.addItems(
            ["Country 1", "Country 2", "Country 3"])
        self._ui.listStates.addItems(["State 1", "State 2", "State 3"])

    def connectWithControllers(self):
        """
        Metodo en cual se conectan todos los eventos de la interfaz con sus respectivos controladores
        """
        # Conectar la lista de paises con su controlador
        self._ui.listCountries.currentTextChanged.connect(
            self._controller.selectCountry)

        # Conectar la lista de ciudades con su controlador
        self._ui.listStates.currentTextChanged.connect(
            self._controller.selectState)

        # Conectar el slider con su controlador
        self._ui.sldAverageDays.valueChanged.connect(
            self._controller.selectRange)

        # Conectar el SpinBox con su controlador
        self._ui.spbRange.valueChanged.connect(
            self._controller.selectRange)

        # Conectar los RadioButtons de opciones de datos con su controlador
        self._ui.rdbCases.toggled.connect(
            self.determineRadioDataOption)
        self._ui.rdbDeaths.toggled.connect(
            self.determineRadioDataOption)
        self._ui.rdbBoth.toggled.connect(
            self.determineRadioDataOption)

        # Conectar los RadioButtons de opciones de datos con su controlador
        self._ui.rdbCumulative.toggled.connect(
            self.determineRadioTypeOption)
        self._ui.rdbDaily.toggled.connect(
            self.determineRadioTypeOption)

    def determineRadioDataOption(self):
        """
        Metodo auxiliar para determinar el RadioButton seleccionado y que devuelva un DataOption
        """
        radioBtn: QRadioButton = self.sender()
        if radioBtn.isChecked():
            self._controller.selectDataOption(
                DataOptions[radioBtn.text().upper()])

    def determineRadioTypeOption(self):
        """
        Metodo auxiliar para determinar el RadioButton seleccionado y que devuelva un TypeOption
        """
        radioBtn: QRadioButton = self.sender()
        if radioBtn.isChecked():
            self._controller.selectDataOption(
                TypeOptions[radioBtn.text().upper()])
