#!/usr/bin/env python
# -*- coding: utf-8 -*-

import enum

from typing import List
from models.models import Earthquake


class TableLength(enum.Enum):
    past_hour = 1
    past_day = 2
    past_7_days = 3
    past_30_days = 4


class TimeValueFormatException(Exception):
    __message = "Format incorrect: '{value}'"

    def __init__(self, value) -> None:
        self.value = value
        super().__init__(self.__message.format(value=value))


class PopulateDate(object):
    def __init__(self, earthquakes: List[Earthquake], ) -> None:
        self.__earthquakes = earthquakes


class TableDesigner(object):

    def __init__(self, x_label: str, y_label: str, table_lenght: TableLength) -> None:
        self.__x_label = x_label
        self.__y_label = y_label
        self.__table_lenght = table_lenght
