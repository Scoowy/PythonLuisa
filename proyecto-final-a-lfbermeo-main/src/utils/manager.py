from datetime import datetime
from src.config.config import PLOT_AREA_TITLE_FORMAT
import pandas as pd
from datetime import datetime

import pyqtgraph as pg
from pyqtgraph.graphicsItems.PlotDataItem import PlotDataItem
from pyqtgraph.graphicsItems.DateAxisItem import DateAxisItem
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

    def __sumarTuplas(self, x) -> tuple:
        inf, det = 0, 0
        for index, value in x.items():
            inf += value[0]
            det += value[1]
        return inf, det

    def getGlobalData(self) -> pd.DataFrame:
        # value = self._df.loc[self._df['State'] == '', :].sum()
        serie = self._df.loc[self._df['State'].isna()].drop(['State'], axis=1)
        newData = serie.apply(lambda x: self.__sumarTuplas(x)).transpose().rename(
            columns={0: 'infections',  1: 'deaths'})
        newData.index = pd.to_datetime(newData.index, format='%m/%d/%y')
        return newData

    def getNewDataFrameFromCountry(self, serie: pd.Series) -> pd.DataFrame:
        data = {"infections": [], "deaths": []}

        for values in serie:
            data["infections"].append(values[0])
            data["deaths"].append(values[1])

        newData = pd.DataFrame(data, index=serie.index)
        newData.index = pd.to_datetime(newData.index, format='%m/%d/%y')

        return newData

    # Revisar uso
    def getSeriesCountry(self, country: str) -> pd.Series:
        return self._df.loc[country][1:]

    def getDataCountry(self, country: str, state=None) -> pd.DataFrame:
        if state == None:
            serie = self._df.loc[country][1:]
            return self.getNewDataFrameFromCountry(serie)
        else:
            # print(country)
            # print(state)
            serie = self._df.loc[country]
            serie.set_index('State', inplace=True)
            return self.getNewDataFrameFromCountry(serie.loc[state])

    def getCountries(self) -> list:
        """
        Metodo que devuelve una lista de paises
        """
        return sorted(list(set(self._df.index.values.tolist())))

    def getStates(self, country: str) -> list:
        """
        Metodo que deveulve una lista de ciudades perteneciente a un pais
        """
        self._df.loc[country]['State'][0] = "Todos"
        # print(self._df.loc[country]['State'])
        return self._df.loc[country]['State'].dropna().values.tolist()

    def getDataDaily(self, data):
        pastInf = 0
        pastDea = 0
        for index in range(0, data.index.size):
            diffInf = data.iloc[index]['infections'] - pastInf
            diffDea = data.iloc[index]['deaths'] - pastDea

            pastInf = data.iloc[index]['infections']
            pastDea = data.iloc[index]['deaths']

            data.iloc[index]['infections'] = diffInf
            data.iloc[index]['deaths'] = diffDea
        return data


class PlotManager(object):
    """
    Clase que implemta metodos para gestionar el Plot
    """

    def __init__(self, plotArea: PlotWidget = None) -> None:
        super().__init__()
        self._plotArea = plotArea
        self._plotInfecctions = PlotDataItem(
            pen=(33, 145, 251), antialias=True)
        self._plotDeaths = PlotDataItem(pen=(219, 58, 52), antialias=True)

    @property
    def plotArea(self) -> PlotWidget:
        """
        plotArea property.
        """
        return self._plotArea

    @plotArea.setter
    def plotArea(self, value: PlotWidget):
        self._plotArea = value

    def changeInfecctionsData(self, data):
        x = [value.timestamp() for value in data.index.to_list()]
        y = data.values.tolist()
        self.p1.plot(x, y, clear=True, pen=(33, 145, 251))

    def changeDeathData(self, data):
        x = [value.timestamp() for value in data.index.to_list()]
        y = data.values.tolist()
        self._plotDeaths.setData(x, y)
        self.p2.addItem(self._plotDeaths)

    def setStylePlotArea(self, backgroundColor=None):
        axisDate = MyTimeAxis(orientation="bottom", utcOffset=10)

        self._plotArea.setBackground(backgroundColor)
        self._plotArea.setTitle(
            "Daily number of Cases and Deaths in Spain (14-day mean)",
            color=(57, 57, 58),
            size="18pt"
        )
        self._plotArea.setAxisItems({'bottom': axisDate})

        self.settear()

    def settear(self):
        styles = {'color': (57, 57, 58), 'font-size': '12px'}

        self.p1 = self._plotArea.plotItem
        self.p1.setLabels(left='Infections')

        self.p1.getAxis('left').setLabel(
            'Infections', **{'color': (33, 145, 251), 'font-size': '12px'})

        # Create a new ViewBox, link the right axis to its coordinate system
        self.p2 = pg.ViewBox()
        self.p1.showAxis('right')
        self.p1.scene().addItem(self.p2)
        self.p1.getAxis('right').linkToView(self.p2)
        self.p2.setXLink(self.p1)
        self.p1.getAxis('right').setLabel(
            'Deaths', **{'color': (219, 58, 52), 'font-size': '12px'})

        self.updateViews()
        self.p1.vb.sigResized.connect(self.updateViews)

    def updateViews(self):
        self.p2.setGeometry(self.p1.vb.sceneBoundingRect())
        self.p2.linkedViewChanged(self.p1.vb, self.p2.XAxis)


class MyTimeAxis(DateAxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        labels = []
        for value in values:
            # print(value)
            labels.append(datetime.fromtimestamp(value).strftime('%d/%m/%y'))
        return labels
