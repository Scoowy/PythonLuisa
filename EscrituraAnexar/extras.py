#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pedirTareas():
    salir = False
    listaTareas = []

    while not salir:
        tarea = input("Tarea: ").strip()

        # Comprobamos que no sea un texto vacio o que solo contenga espacio
        if tarea != "":
            if tarea.lower() != "detener":
                listaTareas.append(tarea)
            else:
                salir = True
        else:
            print("Ingrese nuevamente la tarea...")

    return listaTareas


def pedirNombreLista():
    salir = False
    nombreLista = ""

    while not salir:
        # Pedimos el nombre al usuario
        # Limpiamos los espacios en blanco finales e inicales
        nombre = input("Ingrese el nombre de la lista: ").strip()

        # Remplazamos todos los espacios en blanco intermedios por un "_"
        nombre = nombre.replace(" ", "_")

        # Comprobar que no sea vacio
        if nombre != "":
            # Comprobar que no solo sea ".txt"
            if nombre != ".txt":
                if nombre.find(".txt") >= 0:
                    nombreLista = nombre
                else:
                    nombreLista = nombre + ".txt"

                salir = True
            else:
                print("El nombre no puede ser solo al extension del archivo...")
        else:
            print("El nombre del archivo no es correcto...")

    return nombreLista
