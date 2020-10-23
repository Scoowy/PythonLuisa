#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ui import imprimirLista, listarListasTareas, menuPrincipal
from archivo import escribirArchivo
from extras import pedirTareas, pedirNombreLista


def main():

    salir = False

    while not salir:
        opcionInicial = menuPrincipal()

        if opcionInicial == 1:
            # Abrir una lista de tareas
            lista = listarListasTareas()

            if lista != None:
                imprimirLista(lista)

        elif opcionInicial == 2:
            nombreLista = pedirNombreLista()
            nuevasTareas = pedirTareas()

            escribirArchivo(nombreLista, nuevasTareas)

        else:
            salir = True


if __name__ == "__main__":
    main()
