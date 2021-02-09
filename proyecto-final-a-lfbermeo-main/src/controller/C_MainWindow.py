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

        self._model = model  # Referencia al modelo

    # INICIO Bloque de controladores
    @pyqtSlot(str)
    def selectCountry(self, value):
        """
        Controlador que escucha el evento de cambio en la lista de paises
        """
        if (value != 'Global'):
            # Si es un nombre de pais se almacena en el estado
            self._model.country = value
            # Se comprba si este pais pertenece a los paises especiales con ciudades
            if value in COUNTRIES_WITH_STATES:
                # Si es un pais especial envia el nombre del pais para obenter la lista de ciudades
                self._model.changeStateList(value)
            else:
                # si no es un pais especiela envia None para no obtener ninguma lista de ciudades
                # print(f"Graficar todos los datos de: {value}")
                self._model.changeStateList(None)

        else:
            # Al ser global no tiene ninugn pais entonces se pasa como argumetno None
            self._model.changeStateList(None)
            # Se cargan los datos del total global
            self._model.loadDataFromCountryState(value)

    @pyqtSlot(str)
    def selectState(self, value):
        """
        Controlador que escucha el evento de cambio en la lista de ciudades
        """
        if (value != ''):  # Se comprueba s no es vacio
            self._model.state = value  # Se almacena en el estado el nuevo valor
            if self._model.country in COUNTRIES_WITH_STATES:  # Se compureba pais esecial
                # Si es un pais especial se envia el pais y la ciuded seleccionada
                self._model.loadDataFromCountryState(
                    self._model.country, self._model.state)
            else:
                # De no ser un pais especial se envia unicamente el nombre del pais
                # print("Graficar los datos de todos")
                self._model.loadDataFromCountryState(self._model.country)

    @pyqtSlot(int)
    def selectRange(self, value):
        """
        Controlador que escucha el evento de cambio en el slider de rango
        """
        # Se almacena el nuevo estado del slider
        self._model.rangeValue = value
        # Se llama a graficar nuevamente
        self._model.plotData()

    @pyqtSlot(DataOptions)
    def selectDataOption(self, value):
        """
        Controlador que escucha el evento de cambio en las opciones de:
        - Cases
        - Deaths
        - Both
        """
        # Se alamcena el nuevo estado de dataOption
        self._model.dataOption = value
        # Se llama a graficar nuevamente
        self._model.plotData()

    @pyqtSlot(TypeOptions)
    def selectTypeOption(self, value):
        """
        Controlador que escucha el evento de cambio en las opciones de:
        - Cumulative
        - Daily
        """
        # Se almacena el nuev valor de estado de TypeOptions
        self._model.typeOption = value
        # Se llama agraficar nuevmanete
        self._model.plotData()

    def passPlotWidgetToModel(self, plotWidget: PlotWidget, backgroundColor):
        """
        Metodo que se encarga unicamente de pasar el contexto del grafico desde la vista asta el modelo
        """
        # Se establece el nuevo grafico
        self._model._plotManager.plotArea = plotWidget
        # Se inicializa el grafico con valores or defecto
        self._model._plotManager.setStylePlotArea(
            backgroundColor=backgroundColor)
