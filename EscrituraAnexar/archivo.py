#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def escribirArchivo(archivo: str, listaTareas):
    """
    Funcion que escribe un nuevo archivo u anexa en uno exisente.
    """

    # Direccion relativa
    archivoPath = "./listas/{}".format(archivo)
    # Convertimos el nombre de la lista a un Path de Python
    fileObj = Path(archivoPath)

    # Modo de sobreescritura por defecto
    modoArchivo = "w"

    # Comprobamos que el objeto exite y es un archivo
    if fileObj.is_file():
        # Anexar las tareas
        modoArchivo = "a"

    with fileObj.open(mode=modoArchivo) as f:
        for tarea in listaTareas:
            f.write(tarea + "\n")


def leerArchivo(archivo: Path):
    """
    Funcion que lee un archivo de texto.
    """
    tareas = []

    with archivo.open("r") as f:
        for linea in f:
            tareas.append(linea.replace("\n", ""))

    return (archivo.name, tareas)


def obtenerListas():
    """
    Funcion que retorna una lista de Path's de los archivos de listas.
    """
    dirListas = Path("./listas")
    listasTareas = []

    for fichero in dirListas.iterdir():
        if fichero.name.endswith(".txt"):
            listasTareas.append(Path(fichero))

    return listasTareas
