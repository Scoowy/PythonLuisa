import pandas as pd


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
