from datetime import datetime
import pandas as pd
from datetime import datetime

import pyqtgraph as pg
from pyqtgraph.graphicsItems.PlotDataItem import PlotDataItem
from pyqtgraph.graphicsItems.DateAxisItem import DateAxisItem
from pyqtgraph.widgets.PlotWidget import PlotWidget

# Lista de paises especiales con ciudades
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
        self._df = df  # Estado del dataframe

    # INIICO Bloque de propiedaes
    @property
    def df(self) -> pd.DataFrame:
        """
        df property.
        """
        return self._df

    @df.setter
    def df(self, value):
        self._df = value
    # FIN Bloque de propiedades

    def __sumarTuplas(self, x) -> tuple:
        """
        Metodo 'privado', llamado desde una funcion lambda, que permite sumar sumar 
        todas las tuplas de la columna y retornar asi mismo otra tupla.
        """
        inf, det = 0, 0
        for index, value in x.items():  # Metodo que nos devuelve un idice y el valor
            inf += value[0]
            det += value[1]
        # Retornamos el resultado en forma de tupla
        return inf, det

    def getGlobalData(self) -> pd.DataFrame:
        """
        Metodo que permite obtener un dataframe con los valores globales sobre contagios
        y muertes, para ellos se usa la funcion .apply de pandas apra ejecutar una
        funcion que porcese la informacion, esta funcion se encuentra definida en 
        __sumaTuplas, y se llama mednianet el uso de una funcion anonima (lambda).
        Este metodo sera ustilizado unicamente cuando se requira graficar la informacion
        Global.
        """
        # Se extraen todos las filas que contienen en su columna State un valor NaN o vacio
        # Al revisar la ifnorcion de origen se pudo apreciar que la primera fila
        # de los paises que contienen ciudades pertenece a al suma global de sus ciudades
        # De este modo se omiten todos las filas que coneitnen ciudades, para no repetir datos.
        # A continuacion se elimina la columna State ya que no contiene mas que NaN, siendo
        # inservible.
        serie = self._df.loc[self._df['State'].isna()].drop(['State'], axis=1)

        # Se procede a usar la funcion que sumara las tuplas de valor
        # A continuacion se hace la transpuesta de la matriz, para tener los valores,
        # de infrecciones y muertes como columnas, asi mismo se ressmplaza estos nombres.
        newData = serie.apply(lambda x: self.__sumarTuplas(x)).transpose().rename(
            columns={0: 'infections',  1: 'deaths'})
        # Se porcede a convertir el indice, que es texto asi '1/1/20' a un dato,
        # de tipo datetime
        newData.index = pd.to_datetime(newData.index, format='%m/%d/%y')
        return newData  # Se retornna la nueva data global

    def getNewDataFrameFromCountry(self, serie: pd.Series) -> pd.DataFrame:
        """
        Metood que conforma un nuevo dataFrame, con dos columnas una de infections y otra de deaths, 
        ademas de estables el indice las fechas, a partir de una serie de pandas que,
        se pasa como parametero, al momento de seleciconar un fila.
        Este metodo sera usado por graficar Paises solamente o con sus paises.
        """
        # Se crea un diccionario con listas vacias
        data = {"infections": [], "deaths": []}

        # Se reccorre la serie añadiendo los valores a sus respectivas listas
        for values in serie:
            data["infections"].append(values[0])
            data["deaths"].append(values[1])

        # Se crea un nuevo dataFrame a partir de los datos extraidos anterioremtne
        # Se establece que el indice sera el indece de la serie original
        newData = pd.DataFrame(data, index=serie.index)
        # Se porcede a convertir el indice, que es texto asi '1/1/20' a un dato,
        # de tipo datetime
        newData.index = pd.to_datetime(newData.index, format='%m/%d/%y')

        return newData

    def getDataCountry(self, country: str, state=None) -> pd.DataFrame:
        """
        Metodo que obtiene la data del pais y sus respectiva ciudad si esta es,
        pasada como parametro
        """
        if state == None:  # Si no existe ciudad
            # Se extrae la fila que coincida con el pais
            serie = self._df.loc[country][1:]
            # Se envia al metodo para obtener un dataframe mas a corde
            return self.getNewDataFrameFromCountry(serie)
        else:
            # Si tiene ciudad exatremos todas las ciudades que coinciden con con el pais
            serie = self._df.loc[country]
            # Se reemplaza el indice del pais por la columna State
            serie.set_index('State', inplace=True)
            # Se envia al metodo para obtener un dataframe mas a corde
            return self.getNewDataFrameFromCountry(serie.loc[state])

    def getCountries(self) -> list:
        """
        Metodo que devuelve una lista ordenada de paises
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
        """
        Metodo quese encarga de calcular la variacion en tre un dia y el anterior,
        obatenideno asi valores de cuantos contagios nuevo o muertes se han producido
        en ese dia.
        """
        # variables auxiliares
        pastInf = 0
        pastDea = 0
        for index in range(0, data.index.size):  # Recorremos la data
            # Se calcula la direferecia
            diffInf = data.iloc[index]['infections'] - pastInf
            diffDea = data.iloc[index]['deaths'] - pastDea

            # Se almacena momentaneamente el valor actual
            pastInf = data.iloc[index]['infections']
            pastDea = data.iloc[index]['deaths']

            # Se establece el valor nuevo
            data.iloc[index]['infections'] = diffInf
            data.iloc[index]['deaths'] = diffDea
        return data


class PlotManager(object):
    """
    Clase que implemta metodos para gestionar el Plot
    """

    def __init__(self, plotArea: PlotWidget = None) -> None:
        """
        Constructor de clase
        """
        super().__init__()
        self._plotArea = plotArea  # Area del grafico
        self._plotInfecctions = PlotDataItem(
            pen=(33, 145, 251), antialias=True)  # Objetos que mantedran la informacion
        self._plotDeaths = PlotDataItem(pen=(219, 58, 52), antialias=True)

    # INICIO Bloque propiedaes
    @property
    def plotArea(self) -> PlotWidget:
        """
        plotArea property.
        """
        return self._plotArea

    @plotArea.setter
    def plotArea(self, value: PlotWidget):
        self._plotArea = value
    # FIN Bloque de propiedaes

    def changeInfecctionsData(self, data):
        """
        Metodo que reemplaza los datos anteriores de la grafica por los nuevos
        en los valores de infecciones
        """
        # Se extraen los valoes del indeice para hacerlos etiquetas del eje x
        x = [value.timestamp() for value in data.index.to_list()]
        y = data.values.tolist()
        self.p1.plot(x, y, clear=True, pen=(33, 145, 251))  # Se le da color

    def changeDeathData(self, data):
        """
        Metodo que reemplaza los datos anteriores de la grafica por los nuevos
        en los valores de muertes
        """
        # Se extraen los valoes del indeice para hacerlos etiquetas del eje x
        x = [value.timestamp() for value in data.index.to_list()]
        y = data.values.tolist()
        self._plotDeaths.setData(x, y)
        # Se añade el agrafico al area de dibujo
        self.p2.addItem(self._plotDeaths)

    def setStylePlotArea(self, backgroundColor=None):
        """
        Metodo que dota de estilos inciiales al agrafica, ademas de configuraciones.
        Se configura los ejes de coordenadas sus nombres, y cuantas graficas se van a
        dibujar.
        """
        # Creo una instancia de mi EjeX personalizado para el tiempo
        axisDate = MyTimeAxis(orientation="bottom", utcOffset=10)
        # Se coloca mi EjeX personalizado en la parte inferior
        self._plotArea.setAxisItems({'bottom': axisDate})

        # se establece el titulo y el color de fondo
        self._plotArea.setBackground(backgroundColor)
        self._plotArea.setTitle(
            "Daily number of Cases and Deaths in Spain (14-day mean)",
            color=(57, 57, 58),
            size="18pt"
        )

        # Se configura que la grafica admita dos dbujados de datos
        self.p1 = self._plotArea.plotItem
        self.p1.setLabels(left='Infections')

        self.p1.getAxis('left').setLabel(
            'Infections', **{'color': (33, 145, 251), 'font-size': '12px'})

        # Crea un nuevo ViewBox, que se enlaza la eje derecho del sistema de coordenadas
        # Este contendra las muertes
        self.p2 = pg.ViewBox()
        self.p1.showAxis('right')
        self.p1.scene().addItem(self.p2)
        self.p1.getAxis('right').linkToView(self.p2)
        self.p2.setXLink(self.p1)
        self.p1.getAxis('right').setLabel(
            'Deaths', **{'color': (219, 58, 52), 'font-size': '12px'})

        # Se actualiza el grafico
        self.updateViews()
        # Se vincula el evento de acciones con la actulizacion del grfico
        self.p1.vb.sigResized.connect(self.updateViews)

    def updateViews(self):
        """
        Metodo que es llamadao para redibujar cada ves que el usuario mueva el grafico.
        """
        self.p2.setGeometry(self.p1.vb.sceneBoundingRect())
        self.p2.linkedViewChanged(self.p1.vb, self.p2.XAxis)


class MyTimeAxis(DateAxisItem):
    """
    Clase que representa un eje de cordenadas personalizado,
    por motivo que no entiendo, las fechas se mostraban por defecto de forma incorrecta.
    Se procedio a configurar un nuevo eje de coordenadas que represente el valor
    de fechas en un formato mas comodo.
    """

    def __init__(self, *args, **kwargs):
        """
        constructor de clase
        """
        super().__init__(*args, **kwargs)
        # self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        """
        Metodo sobreescrito de DateAxisItem, que nos permite establecer el formato
        con el cual se representara los valores del eje x
        """
        labels = []
        for value in values:
            # Convertimos el Timestamp del Datetime del eje x
            # Y lo formateamos a '01/01/20'
            labels.append(datetime.fromtimestamp(value).strftime('%d/%m/%y'))
        return labels
