from src.config.config import PLOT_AREA_TITLE_FORMAT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

import pyqtgraph as pg
from pyqtgraph.graphicsItems.PlotDataItem import PlotDataItem
from pyqtgraph.widgets.PlotWidget import PlotWidget


COUNTRIES_WITH_STATES = [
    'Australia',
    'Canada',
    'China',
    'Denmark',
    'France',
    'Netherlands',
    'United Kingdom',
    'United States',
]


class DataManager(object):
    """
    Clase que provee de metodos para segmentar y trabajar con la iformacion del Dataframe
    """

    def __init__(self, df: pd.DataFrame = None) -> None:
        """
        Constructor
        """
        super().__init__()
        self._df = df

    @property
    def df(self) -> pd.DataFrame:
        """
        df property.
        """
        return self._df

    @df.setter
    def df(self, value):
        self._df = value

    def getNewDataFrameFromCountry(serie: pd.Series) -> pd.DataFrame:
        data = {"infections": [], "deaths": []}

        for values in serie:
            data["infections"].append(values[0])
            data["deaths"].append(values[1])

        return pd.DataFrame(data, index=serie.index)

    def getSeriesCountry(self, country: str) -> pd.Series:
        return self._df.loc[country][1:]

    def getDataCountry(self, seriesCountry: pd.Series) -> pd.DataFrame:
        return self.getNewDataFrameFromCountry(seriesCountry)

    def getCountries(self) -> list:
        """
        Metodo que devuelve una lista de paises
        """
        return sorted(list(set(self._df.index.values.tolist())))

    def getStates(self, country: str) -> list:
        """
        Metodo que deveulve una lista de ciudades perteneciente a un pais
        """
        return self._df.loc[country]['State'].dropna().values.tolist()


class PlotManager(object):
    """
    Clase que implemta metodos para gestionar el Plot
    """

    def __init__(self, plotArea: PlotWidget = None) -> None:
        super().__init__()
        self._plotArea = plotArea
        self._plotInfecctions = PlotDataItem()
        self._plotDeaths = PlotDataItem()
        # pg.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        # self._plotero: Figure = plt.figure()

    @property
    def plotArea(self) -> PlotWidget:
        """
        plotArea property.
        """
        return self._plotArea

    @plotArea.setter
    def plotArea(self, value: PlotWidget):
        self._plotArea = value

    def setStylePlotArea(self):
        # colorDefault = self.palette().color(QtGui.QPalette.Window)
        # Titulo de la grafica
        self._plotArea.setTitle(PLOT_AREA_TITLE_FORMAT.format(
            {"country": "ALL", "average": 1}))
