#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import stat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import us


def cleanStates(x):
    if x:
        return "EE.UU" if us.states.lookup(x.strip()) else x.strip()
    else:
        return x


def cleanPlace(x: str):
    trash = ["southern", "western", "eastern", "northern",
             "of", "south", "west", "east", "north", "the", "region", "central"]

    if x:
        if x.strip() != "":
            tokens = x.split(",")

            for token in tokens:
                for retoken in token.split(" "):
                    state = us.states.lookup(retoken)
                    if state != None:
                        return state.name

            pais = tokens[-1]
            newPais = []
            for token in pais.split(" "):
                if token.lower() not in trash:
                    newPais.append(token)

            return ' '.join(newPais).strip()
        else:
            return x.strip()
    else:
        return ""


data_df = pd.read_csv("usgs_terremotos_2014.csv",
                      index_col="id", parse_dates=["time", "updated"])
data_df.dropna(axis=0, subset=["place"], inplace=True)


isEmpty = data_df["place"].apply(lambda x: x.strip() == "")
data_df = data_df.drop(data_df[isEmpty].index)

# data_df["pais"] = data_df["place"].str.split(",", n=2, expand=True)[1]
data_df["pais"] = data_df["place"].apply(lambda x: cleanPlace(x))

data_df["pais"] = data_df["pais"].apply(lambda x: cleanStates(x))

byPais = data_df[['pais', 'mag']].groupby(['pais'])['mag'].describe()

# TOP 10 por num de terremotos
top10numTerr = byPais[['count']].sort_values("count", ascending=False)[:10]
# print(top10numTerr)

# Top 10 max magnitud
top10maxMag = byPais[['max']].sort_values("max", ascending=False)[:10]
# print(top10maxMag)

# Top 10 min magnitud
top10minMag = byPais[['min']].sort_values("min", ascending=True)[:10]
# print(top10minMag)


# Filtro de magnitud 4 o superior
isMore4Mag = data_df['mag'] >= 4

by4Magnitud = data_df[isMore4Mag]

print(by4Magnitud.sample(5))
