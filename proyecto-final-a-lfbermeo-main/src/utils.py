from datetime import datetime
import re

import pandas as pd
from pandas.core.frame import DataFrame

from .models import Country, Register, State


def cargarDatos(path: str, index="Country"):
    """
    Metodo que se encarga de comprobar y obtner los datos de un archivo.
    """
    try:
        return pd.read_csv(path, index_col=index)
    except Exception as err:
        print(err)
        return None


def prepareData(df: DataFrame, rangeCol=[11], stateNan="ALL"):
    """
    Metodo que devuelve un dataframe con datos preparados.
    ---
    Los valores NaN en la columna de State se transforman a ALL
    se puede limitar el numero de columnas del dataframe mediante
    el parametro rangeCol.
    """
    df = df.iloc[:, [col for col in range(*rangeCol)]]
    df["State"].fillna("ALL", inplace=True)

    return df


def passDfToObjects(df: DataFrame):
    columns = df.columns
    stateCol = columns[0]
    columns = columns.drop(stateCol)
    countries = df.index

    patternValues = re.compile(r"(\d+)(\s+)(\d+)")
    patternDate = re.compile(r"(\d+)/(\d+)/(\d+)")

    countriesDict = {}

    # Recorremos las filas
    for countrieName in countries:
        countryObj = None
        stateObj = None

        # Comprobamos que el nombre del Country existe en el diccionario de countries
        if countrieName not in countriesDict:
            # Si no existe creamos un par clave valor con el nombre del country y un objeto country.
            countriesDict[countrieName] = Country(countrieName)

        countryObj = countriesDict[countrieName]

        stateName = df[stateCol][countrieName]

        # Comprobamos que el valor extreido es un objeto Series de pandas
        if type(stateName) is str:
            states = [stateName]
        else:
            print(stateName)
            states = stateName.values

        for stateName in states:
            if stateName not in countryObj.getStates():
                countryObj.getStates()[stateName] = State(stateName)

            stateObj = countryObj.getStates()[stateName]

            for column in columns:
                # Convertimos el nombre de la columna en un datetime
                matchDate = patternDate.match(column)
                month, day, year = matchDate.groups()
                # Convertimos los valores a numeros enteros
                month = int(month)
                day = int(day)
                year = int(f"20{year}")

                # Extraemos los valores de la tupla de contagios y muertes
                value = df[column][countrieName]
                matchValues = patternValues.match(value)
                infections, _, deaths = matchValues.groups()
                infections = int(infections)
                deaths = int(deaths)

                stateObj.addRegister(
                    Register(datetime(year, month, day), infections, deaths))

    return countriesDict
