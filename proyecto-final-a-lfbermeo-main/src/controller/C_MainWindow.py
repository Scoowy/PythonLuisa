from PyQt5.QtCore import QObject, pyqtSlot
from pyqtgraph.widgets.PlotWidget import PlotWidget
from src.model.M_MainWindow import MainModel
from src.utils.enums import DataOptions, TypeOptions


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
        print(value)

    @pyqtSlot(str)
    def selectState(self, value):
        """
        Controlador que escucha el evento de cambio en la lista de ciudades
        """
        print(value)

    @pyqtSlot(int)
    def selectRange(self, value):
        """
        Controlador que escucha el evento de cambio en el slider de rango
        """
        print(value)
        self._model.rangeValue = value

    @pyqtSlot(DataOptions)
    def selectDataOption(self, value):
        """
        Controlador que escucha el evento de cambio en las opciones de:
        - Cases
        - Deaths
        - Both
        """
        print(value)

    @pyqtSlot(TypeOptions)
    def selectTypeOption(self, value):
        """
        Controlador que escucha el evento de cambio en las opciones de:
        - Cumulative
        - Daily
        """
        print(value)

    def passPlotWidgetToModel(self, plotWidget: PlotWidget):
        pass
