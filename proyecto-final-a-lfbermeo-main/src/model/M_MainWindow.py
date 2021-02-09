import pandas as pd
from src.utils.manager import DataManager, PlotManager
from src.utils.reader import ReaderData
from src.config.config import CSV_PATH
from PyQt5.QtCore import QObject, pyqtSignal
from src.utils.enums import DataOptions, TypeOptions


class MainModel(QObject):
    """
    Model para la vista principal
    """

    # Variables "bandera" que emiten señales de eventos
    rangeValueChanged = pyqtSignal(int)
    statesListChanged = pyqtSignal(list)

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

        # Atributos de clase
        self._country = ''  # Almacena el pais
        self._state = ''  # Almacena la ciduad
        self._rangeValue = 1  # Almacena el valor del Slider
        self._stateList = []  # Almacena la lista de ciudades
        self._data = None  # Alamcena la adata actual
        self._typeOption = TypeOptions.CUMULATIVE  # Almacena el tipo de grafica
        # Almacena que graficas mostrar // No implementado
        self._dataOption = DataOptions.BOTH
        # Instancia del manejador de la grafiaca
        self._plotManager = PlotManager()
        # Instancia del manejador de los datos
        # Se hace uso de la clase ReaderData para obtneer el dataframe principal
        self._dataManager = DataManager(
            ReaderData(CSV_PATH).getDataframe())

    # INICIO Bloque de propiedades
    @property  # "Getter" del atributo _rangeValue
    def rangeValue(self) -> int:
        """
        rangeValue property.
        """
        return self._rangeValue

    @rangeValue.setter  # "Setter" del atributo _rangeValue
    def rangeValue(self, value):
        self._rangeValue = value
        # Se emite una señal de que el valor actual a sido modificado
        self.rangeValueChanged.emit(self._rangeValue)

    @property
    def stateList(self) -> list:
        """
        stateList property.
        """
        return self._stateList

    @stateList.setter
    def stateList(self, list):
        self._stateList = list
        self.statesListChanged.emit(self._stateList)

    @property
    def country(self) -> str:
        """
        country property.
        """
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def state(self) -> str:
        """
        state property.
        """
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def data(self) -> pd.DataFrame:
        """
        data property.
        """
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def typeOption(self) -> TypeOptions:
        """
        typeOption property.
        """
        return self._typeOption

    @typeOption.setter
    def typeOption(self, value):
        self._typeOption = value

    @property
    def dataOption(self) -> DataOptions:
        """
        dataOption property.
        """
        return self._dataOption

    @dataOption.setter
    def dataOption(self, value):
        self._dataOption = value

    # FIN Bloque de propiedades

    def getCountryList(self) -> list:
        """
        Metodo que se encarga de obtener los paises desde el mannejador de datos
        """
        countryList = ["Global"]
        return countryList + self._dataManager.getCountries()

    def getStateList(self) -> list:
        """
        Metodo que se encarga de establecer por defecto una lista de ciudades
        """
        stateList = ["Todos"]
        return stateList

    def changeStateList(self, country: str) -> list:
        """
        Metodo que se encarga de obtener las ciudades desde el manejador de datos.
        Metodo que es llamado cada vez que un pais es seleccionado.
        """
        if country == None:
            self.stateList = ["Todos"]
            # El primer valor de los paises con ciudades, se identifico como el
            # "Todos", ya que contiene la suma de todoas las ciudades de su pais.
        else:
            # Si el pais es uno con ciudades se procede a actualizar la lista
            self.country = country
            data = self._dataManager.getStates(country)
            self.stateList = data

    def loadDataFromCountryState(self, country: str, state=None):
        """
        Metodo que se encarga de cargar los datos a graficar.
        Se pide dos parametros country para el pais, y state para la ciudad,
        en el caso de la ciudad se establece podefecto en None, ya que la mayoria
        de paises no poseen datos de sus cidudades.
        """
        if country == "Global":  # Se comprueba si los datos a graficar son lo sglobales
            # Se elimina por ulltimo cualquier rastro de valores NaN
            self.data = self._dataManager.getGlobalData().dropna()
        else:
            # En el caso de no set la opcion global se procede a obtener la data del
            # pais que este seleccionado
            self.data = self._dataManager.getDataCountry(
                country, state).dropna()

        # Se llama a la funcion que permite presentar y actualizar la grafica
        self.plotData()

    def plotData(self):
        """
        Metodo que permite presentar y actualizar la grafica mediante el Plot Manger
        """
        # Se comprueba que tipo de datos se desea mostrar
        # Diarios o acumulativos, por defecto son acmulativos
        if self.typeOption == TypeOptions.DAILY:
            # Si es a diario, se envian al Data Manager para calcular
            # el numero de contagios y muertes por dia.
            data = self._dataManager.getDataDaily(
                self._data.copy())  # Se envia una copia
        else:
            # Si es acumulativo solamente se pasan los datos actuales
            data = self._data

        # Tomano en cuenta el valor en el cual se encuetre el "Slider",
        # Se realiza la media variable, tomando como ventana este valor.
        # Si es 1 no sufre cambios, maximo asta 15
        data = data.rolling(window=self.rangeValue).mean()

        # Por ultimo se pasan los datos de las columnas infections y deaths
        # Al Plot Manager, para que se dibujen en la grafica.
        self._plotManager.changeInfecctionsData(data['infections'])
        self._plotManager.changeDeathData(data['deaths'])
