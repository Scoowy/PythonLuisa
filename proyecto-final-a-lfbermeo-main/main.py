#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.utils import cargarDatos, prepareData, passDfToObjects


def main():
    df = cargarDatos("data/covid_data.csv")

    if df is not None:
        df = prepareData(df, rangeCol=[3])
        print(df.head())
        countries = passDfToObjects(df)

        print(countries)

    else:
        print("No cargo correctamente")


if __name__ == "__main__":
    main()
