#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd


def cargarDatos(archivo):
    try:
        df = pd.read_csv(archivo)
        return df
    except FileNotFoundError as err:
        print("Nombre del archivo incorrecto.")
        return None


def imprimirFilas(df):
    print(df[[2, -3]])


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
            'Opciones:\n1 Imprimir filas\n2 Menor precio\3ordenar\4Estadisticos\5Filtrado')
        res = int(input("Ingrese una opcion: ").strip())
        if res != "" and res > 0 and res < 6:
            if res == 1:
                imprimirFilas(df)
            elif res == 2:
                pass
            elif res == 3:
                pass
            elif res == 4:
                pass
            elif res == 5:
                pass
        else:
            print("Ingrese una opcion correcta.")
    cargarDatos("info_autos.csv")


if __name__ == "__main__":
    main()
