import re
from typing import Pattern


# Completar la función obtenerCorreos para que tome una cadena a la que desea aplicar la expresión regular.
# La función debe devolver una lista con todos los correos electrónicos que terminan en @utpl.edu.ec
def obtenerCorreos(cadena):
    patter = re.compile(r"\w+@utpl.edu.ec")
    return patter.findall(cadena)

# Completar la función obtenerHoras para que tome una cadena a la que desea aplicar la expresión regular.
# La función debe devolver una lista con todas las horas escritos de cinco caracteres HH:MM, donde las horas
# varían de 00 a 23 y los minutos de 00 a 59.


def obtenerHoras(cadena):
    pattern = re.compile(r"[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")
    return pattern.findall(cadena)

# Completar la función obtenerCursos para que tome una cadena a la que desea aplicar la expresión regular.
# La función debe devolver una lista con todos los códigos de cursos de la Universidad Técnica Particular de Loja
# Los códigos de curso como CSCI0180, MCM0340 y CSCI1975F son todos validos.


def obtenerCursos(cadena):
    pattern = re.compile(r"[A-Z]{3,4}\d{4}[A-Z]?")
    return pattern.findall(cadena)
