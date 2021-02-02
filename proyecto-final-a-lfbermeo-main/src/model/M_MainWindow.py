from src.utils.manager import DataManager, PlotManager
from src.utils.reader import ReaderData
from PyQt5.QtCore import QObject, pyqtSignal


class MainModel(QObject):
    """
    Model para la vista principal
    """
    rangeValueChanged = pyqtSignal(int)
    statesListChanged = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self._rangeValue = 1
        self._stateList = []
        self._plotManager = PlotManager()
        self._dataManager = DataManager(
            ReaderData('data/covid_data.csv').getDataframe())

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

    def getCountryList(self) -> list:
        countryList = ["Global"]
        return countryList + self._dataManager.getCountries()

    def getStateList(self) -> list:
        stateList = ["Todos"]
        return stateList

    def changeStateList(self, country: str) -> list:
        if country == None:
            self.stateList = ["Todos"]
        else:
            data = self._dataManager.getStates(country)
            self.stateList = ["Todos"] + data
