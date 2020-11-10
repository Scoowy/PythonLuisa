#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

dfIris = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(dfIris)


def calcDoble(valor):
    return valor * 2


dfIris['DobleAncho'] = dfIris['petal_width'].apply(lambda x: calcDoble(x))
print(dfIris)
