from PyQt5 import QtGui
from src.utils.enums import DataOptions, TypeOptions
from src.view.MainWindow_ui import Ui_MainWindow
from src.model.M_MainWindow import MainModel
from src.controller.C_MainWindow import MainController
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QRadioButton
# from src.utils.manager import Canvas, PlotManager
from pyqtgraph import PlotDataItem


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

        self.stylingPlot()

        self.initializeValues()
        self.connectWithControllers()
        self.connectWithModels()

    def initializeValues(self):
        """
        Metodo en el cual se inicializan algunos valores
        """
        self._ui.listCountries.addItems(
            ["Country 1", "Country 2", "Country 3"])
        self._ui.listStates.addItems(["State 1", "State 2", "State 3"])

        self._controller.passPlotWidgetToModel(self._ui.pnlPlot)

        # self._ui.pnlPlot.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        # self._ui.pnlPlot.plot([0, 1, 2, 3, 4], [2, 5, 12, 7, 34])

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
        pass

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

    def stylingPlot(self):
        colorDefault = self.palette().color(QtGui.QPalette.Window)
        plot = self._ui.pnlPlot

        plot.setBackground(colorDefault)
        plot.setTitle(
            "Daily number of Cases and Deaths in Spain (14-day mean)",
            color=(57, 57, 58),
            size="18pt"
        )

        styles = {'color': (57, 57, 58), 'font-size': '12px'}
        plot.setLabel('left', 'Infections', **styles)
        plot.setLabel('right', 'Deaths', **styles)
        plot.showGrid(x=False, y=True)
        plot2 = PlotDataItem([0, 1, 2, 8], [48, 57, 14, 3], antialias=True)
        plot.addItem(plot2)
