import pandas as pd
import re

from src.config.config import CSV_INDEX_COL, CSV_PATTER_TUPLE_VALUES, CSV_SEPARATOR


class ReaderData(object):
    """
    Clase que implementa metodos para la lectura, procesamiento y obtencion de la informacion dentro de un csv
    """

    def __init__(self, pathfile: str) -> None:
        """
        Constructor de clase
        """
        super().__init__()
        self._pathfile = pathfile
        self._df = None
        self._patternValues = re.compile(CSV_PATTER_TUPLE_VALUES)

    def _loadCSVFile(self):
        """
        Lectura de los datos
        ---
        Se usa el metodo `.read_csv()`, para leer el aarchivo que contiene los datos en formato csv.
        Adicionamos el parametro `index_col` al metodo, que nos permite decirle a **Pandas** que columna queremos que sea el indice de las filas.  
        """
        self._df = pd.read_csv(
            self._pathfile, sep=CSV_SEPARATOR, index_col=CSV_INDEX_COL)

    def _cleanProcessDf(self):
        """
        Limpieza de datos
        ___
        Metodo encargado de procesar la informacion cruda del CSV para un correcto uso.
        """
        # Se applica la funcion a todo el DataFrame exepto la columna "State"
        self._df.iloc[:, 1:] = self._df.iloc[:, 1:].applymap(
            lambda x: self._extractTuples(x))

    def _extractTuples(self, value, pos=0):
        """
        Extraccion de tuplas.
        ---
        Se identifica que los valores se encuntran en un string en formato `[numero][n spacios][numero]`, 
        usando una expresion regular se extraen los valores y se convierten en tuplas `(contagios, muertes)`, 
        despues se extrae cada uno de estos valores en una columan distinta.
        """
        matchValues = self._patternValues.match(value)
        infections, _, deaths = matchValues.groups()
        infections = int(infections)
        deaths = int(deaths)
        return infections, deaths

    def getDataframe(self):
        """
        Metodo que devuelve el dataframe procesado
        """
        self._loadCSVFile()
        self._cleanProcessDf()
        return self._df
