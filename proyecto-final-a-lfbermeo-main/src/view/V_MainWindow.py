from PyQt5 import QtGui
from src.utils.enums import DataOptions, TypeOptions
from src.view.MainWindow_ui import Ui_MainWindow
from src.model.M_MainWindow import MainModel
from src.controller.C_MainWindow import MainController
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QRadioButton


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
        self.connectWithModels()

    def initializeValues(self):
        """
        Metodo en el cual se inicializan algunos valores
        """
        self._ui.listCountries.addItems(
            self._model.getCountryList())
        self._ui.listStates.addItems(self._model.getStateList())

        self._controller.passPlotWidgetToModel(
            self._ui.pnlPlot, self.palette().color(QtGui.QPalette.Window))

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

        # Conectar el valor del LcdDisplay con el valor del slider
        self._ui.sldAverageDays.valueChanged.connect(
            self._ui.lcdRange.display)

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

    def connectWithModels(self):
        self._model.rangeValueChanged.connect(self.onRangeValueChanged)
        self._model.statesListChanged.connect(self.onStatesListChanged)

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
            self._controller.selectTypeOption(
                TypeOptions[radioBtn.text().upper()])

    @pyqtSlot(int)
    def onRangeValueChanged(self, value):
        print(value)

    @pyqtSlot(list)
    def onStatesListChanged(self, value):
        self._ui.listStates.clear()
        self._ui.listStates.addItems(value)
        self._ui.listStates.setCurrentRow(0)
