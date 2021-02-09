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
    rangeValueChanged = pyqtSignal(int)
    statesListChanged = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self._country = ''
        self._state = ''
        self._rangeValue = 1
        self._stateList = []
        self._data = None
        self._typeOption = TypeOptions.CUMULATIVE
        self._dataOption = DataOptions.BOTH
        self._plotManager = PlotManager()
        self._dataManager = DataManager(
            ReaderData(CSV_PATH).getDataframe())

    @property
    def rangeValue(self) -> int:
        """
        rangeValue property.
        """
        return self._rangeValue

    @rangeValue.setter
    def rangeValue(self, value):
        self._rangeValue = value
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

    def getCountryList(self) -> list:
        countryList = ["Global"]
        return countryList + self._dataManager.getCountries()

    def getStateList(self) -> list:
        stateList = ["Todos"]
        return stateList

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

    def changeStateList(self, country: str) -> list:
        if country == None:
            self.stateList = ["Todos"]
            # Calcular la suma de todos
        else:
            # self.country = country
            data = self._dataManager.getStates(country)
            self.stateList = data

    def loadDataFromCountryState(self, country: str, state=None):
        if country == "Global":
            self.data = self._dataManager.getGlobalData().dropna()
        else:
            self.data = self._dataManager.getDataCountry(
                country, state).dropna()

        self.plotData()

    def plotData(self):
        print(self._typeOption)
        if self.typeOption == TypeOptions.DAILY:
            data = self._dataManager.getDataDaily(self._data.copy())
        else:
            data = self._data

        data = data.rolling(window=self.rangeValue).mean()

        self._plotManager.changeInfecctionsData(data['infections'])
        self._plotManager.changeDeathData(data['deaths'])
