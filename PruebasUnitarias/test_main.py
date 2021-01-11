from notero import Note, Notero
from unittest import TestCase


class TestNotero(TestCase):
    def setUp(self) -> None:
        self.notero = Notero()
        self.titulo = "Titulo 1"
        self.contenido = "Contenido"
        return super().setUp()

    def test_aniadir_nueva_nota(self):
        nuevaNota = Note("Nota 1", "Contenido 1")
        self.notero.addNote(nuevaNota)
        self.assertEqual(self.notero.numNotes(), 1,
                         "El numero de notas no coincide")

    def test_eliminar_nota(self):
        self.notero.addNote(Note("Titulo largo", "Contendio largo"))
        notaEliminada = self.notero.deleteNote("N1")
        self.assertTrue(notaEliminada, "La nota no a sido eliminada")
