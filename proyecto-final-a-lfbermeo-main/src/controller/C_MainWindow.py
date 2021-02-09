from PyQt5.QtCore import QObject, pyqtSlot
from pyqtgraph.widgets.PlotWidget import PlotWidget
from src.model.M_MainWindow import MainModel
from src.utils.enums import DataOptions, TypeOptions
from src.utils.manager import COUNTRIES_WITH_STATES


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

    @pyqtSlot(str)
    def selectCountry(self, value):
        """
        Controlador que escucha el evento de cambio en la lista de paises
        """
        if (value != 'Global'):
            self._model.country = value
            if value in COUNTRIES_WITH_STATES:
                self._model.changeStateList(value)
            else:
                print(f"Graficar todos los datos de: {value}")
                self._model.changeStateList(None)

        else:
            self._model.changeStateList(None)
            print("Graficar los datos globales")
            self._model.loadDataFromCountryState(value)

    @pyqtSlot(str)
    def selectState(self, value):
        """
        Controlador que escucha el evento de cambio en la lista de ciudades
        """
        if (value != ''):
            self._model.state = value
            if self._model.country in COUNTRIES_WITH_STATES:
                # if (value != 'Todos'):
                print(f"Graficar datos de {value}")
                self._model.loadDataFromCountryState(
                    self._model.country, self._model.state)
            else:
                print("Graficar los datos de todos")
                self._model.loadDataFromCountryState(self._model.country)

    @pyqtSlot(int)
    def selectRange(self, value):
        """
        Controlador que escucha el evento de cambio en el slider de rango
        """
        self._model.rangeValue = value
        self._model.plotData()

    @pyqtSlot(DataOptions)
    def selectDataOption(self, value):
        """
        Controlador que escucha el evento de cambio en las opciones de:
        - Cases
        - Deaths
        - Both
        """
        self._model.dataOption = value
        self._model.plotData()

    @pyqtSlot(TypeOptions)
    def selectTypeOption(self, value):
        """
        Controlador que escucha el evento de cambio en las opciones de:
        - Cumulative
        - Daily
        """
        self._model.typeOption = value
        self._model.plotData()

    def passPlotWidgetToModel(self, plotWidget: PlotWidget, backgroundColor):
        self._model._plotManager.plotArea = plotWidget
        self._model._plotManager.setStylePlotArea(
            backgroundColor=backgroundColor)
