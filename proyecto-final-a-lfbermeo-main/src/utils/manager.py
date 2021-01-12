import pandas as pd
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class DataManager(object):
    """
    Clase que provee de metodos para segmentar y trabajar con la iformacion del Dataframe
    """

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Constructor
        """
        super().__init__()
        self._df = df

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
        return set(self._df.index.values.tolist())

    def getStates(self) -> list:
        """
        Metodo que deveulve una lista de ciudades perteneciente a un pais
        """
        pass


class PlotManager(object):
    """
    Clase que implemta metodos para gestionar el Plot
    """

    def __init__(self) -> None:
        super().__init__()
        self._plotero: Figure = plt.figure()

    def pruebaPlot(self, sampleGroup):
        # title = f"Daily number of Cases and Deaths in {sampleGroup.name} (14-day mean)"
        # plt.title(title)

        # afgI = sampleData.infections.plot(x=xLabels, kind="area", legend=True)
        # afgI.set_ylabel("Infections")
        # afgI.set_ylim(bottom=0)
        # afgI.set_xlabel("da")

        # afgD = sampleData.deaths.plot(
        #     x=xLabels, secondary_y=True, kind="line", legend=True)
        # afgD.set_ylabel("Deaths")
        # afgD.set_ylim(bottom=0)
        pass


class Canvas(FigureCanvas):
    """
    Clase que reprensenta el canvas donde se dibujara el grafico
    """

    def __init__(self):
        # Codigo para generar la grafica
        # self.figura = Figure()
        # self.ejes = self.figura.add_subplot(111)
        # self.tiempo = np.arange(0.0, 5.65, 0.01)
        # # Calculo de la posicion en el eje X y Y
        # self.x = fx(self.tiempo)
        # self.y = fy(self.tiempo)
        # # Se crea la grafica
        # self.ejes.plot(self.x, self.y)
        # # inicializar el lienzo donde se crea la grafica.
        # FigureCanvas.__init__(self, self.figura)
        pass
