#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Note(object):
    def __init__(self, titulo: str, contenido: str) -> None:
        self.titulo = titulo
        self.contenido = contenido

    def __str__(self) -> str:
        return f"{self.titulo}\n\t{self.contenido}\n"


class Notero(object):
    def __init__(self):
        self.notes = {}

    def addNote(self, note: Note):
        last = len(self.notes) if len(self.notes) > 0 else 1
        self.notes[f"N{last}"] = note

    def deleteNote(self, note: str):
        if self.notes.get(note):
            del self.notes[note]
            return True
        else:
            print(f"La nota {note} no existe.")
            return False

    def numNotes(self):
        return len(self.notes)

    def printNotes(self):
        print(f"===== NOTAS =====")
        for index, note in self.notes.items():
            print(f"{index}:{note}")
        print("="*10)
        print("\n\n")
