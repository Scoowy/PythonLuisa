#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from .service import TimeValueFormatException


class Earthquake(object):
    """
    Class for represent earthqueakes.
    """

    def __init__(self, magnitud: float, place: str, time: datetime = None, ) -> None:
        self.__magnitud = magnitud
        self.__place = place
        self.__time = time

    @property
    def magnitud(self) -> float:
        "Magnitud property."
        return self.__magnitud

    @magnitud.setter
    def magnitud(self, value):
        self.__magnitud = value

    @property
    def place(self) -> str:
        "Place property."
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value

    @property
    def time(self) -> float:
        "Time property."
        return self.__time

    # @time.setter
    # def time(self, value: datetime):
    #     self.__time = value

    @time.setter
    def time(self, value: any):
        if type(value) is datetime:
            self.__time = value
        elif type(value) is int:
            self.__time_from_timestamp(value/1000)
        elif type(value) is float:
            self.__time_from_timestamp(value)
        else:
            raise TimeValueFormatException(value)

    def __time_from_timestamp(self, timestamp: float):
        try:
            self.__time = datetime.fromtimestamp(timestamp)
        except Exception as e:
            print(e)
            return None

    def __str__(self) -> str:
        return '{} {} {}'.format(self.__magnitud, self.__place, self.__time)
