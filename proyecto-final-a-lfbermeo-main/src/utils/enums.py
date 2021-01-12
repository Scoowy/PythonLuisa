import enum


class DataOptions(enum.Enum):
    """
    Clase enum de las opciones posibles para la data a graficar
    """
    CASES = 1
    DEATHS = 2
    BOTH = 3


class TypeOptions(enum.Enum):
    """
    Clase enum de las opciones posibles para el typo de grafica
    """
    CUMULATIVE = 1
    DAILY = 2
