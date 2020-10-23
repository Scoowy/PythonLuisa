#!/usr/bin/env python
# -*- coding: utf-8 -*-

from archivo import leerArchivo, obtenerListas
from pathlib import Path


def pedirOpcion(minOpt: int, maxOpt: int):
    while True:
        opt = input("Opcion: ")

        try:
            opt = int(opt)

            if opt >= minOpt and opt <= maxOpt:
                return opt
            else:
                print("Ingrese una opcion correcta...")
        except ValueError as err:
            print("Ingrese un numero valido...")


def listarListasTareas():
    listas = obtenerListas()

    print("\n====== Listas de tareas ======")

    for indice, lista in enumerate(listas):
        linea = "{}. {}".format(indice+1, lista.name)
        print(linea)

    print("{}. {}".format(len(listas)+1, "Salir"))
    print("==============================")

    opcion = pedirOpcion(1, len(listas)+1)

    if opcion > len(listas):
        return None
    return listas[opcion-1]


def imprimirLista(archivo: Path):
    nombreLista, tareas = leerArchivo(archivo)
    print("\n======================")
    print("Lista: {}".format(nombreLista))
    print("----------------------")
    for tarea in tareas:
        print(tarea)
    print("======================")
    input("\nPulsa ENTER para regresar al menu...")


def menuPrincipal():
    menu = """ 
    ============ MENU ============
    1. Abrir lista de tareas.
    2. Crear o añadir tareas.
    3. Salir.
    ==============================
    """

    print(menu)
    opcion = pedirOpcion(1, 3)

    return opcion
