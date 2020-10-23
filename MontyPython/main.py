#!/usr/bin/env python
# -*- coding: utf-8 -*-

def crear_lista_reparto(archivo: str):
    lista_reparto = []

    with open(archivo) as f:
        for linea in f:
            nombre = linea.replace("\n", "").split(",")[0]
            lista_reparto.append(nombre)

    return lista_reparto


def main():
    cast_list = crear_lista_reparto('reparto_circo_volador.txt')

    for actor in cast_list:
        print(actor)


if __name__ == "__main__":
    main()
