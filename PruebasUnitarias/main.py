#!/usr/bin/env python
# -*- coding: utf-8 -*-

from notero import Note, Notero


def main():
    notero = Notero()
    nota1 = Note("Primera cosa", "Algo que hacer primero")

    notero.addNote(nota1)

    notero.printNotes()

    notero.deleteNote("N1")

    notero.printNotes()


if __name__ == "__main__":
    main()
