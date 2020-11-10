#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas.core.frame import DataFrame


def cargarDatos(archivo):
    try:
        df = pd.read_csv(archivo)
        return df
    except FileNotFoundError as err:
        print("Nombre del archivo incorrecto.")
        return None


def imprimirFilas(df):
    print(df.iloc[[2, -3, -2, -1]])


def datosEstadisticos(df):
    print(df.describe())


def filtradoCaballos(df):
    isCaballos = df['horsepower'] < 100
    dfCaballos = df[isCaballos]

    print(dfCaballos)


def noImplementado():
    print("No implementado")


def main():
    while True:
        archivo = input("Ingrese el nombre del archivo: ").strip()

        if archivo != "":
            df = cargarDatos(archivo)
            break
        else:
            print("Ingrese un nombre valido.")

    while True:
        print(
            'Opciones:\n1 Imprimir filas\n2 Menor precio\n3 ordenar\n4 Estadisticos\n5 Filtrado\n0 Salir')
        res = int(input("Ingrese una opcion: ").strip())
        if res != "" and res >= 0 and res <= 5:
            if res == 1:
                imprimirFilas(df)
            elif res == 2:
                noImplementado()
            elif res == 3:
                noImplementado()
            elif res == 4:
                datosEstadisticos(df)
            elif res == 5:
                filtradoCaballos(df)
            elif res == 0:
                break
        else:
            print("Ingrese una opcion correcta.")
    cargarDatos("info_autos.csv")


if __name__ == "__main__":
    main()
