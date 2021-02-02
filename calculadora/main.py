#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from src.model import CalculatorModel
from src.controller import CalculatorController
from src.view import CalculatorView


class Calculator(QApplication):
    """
    Clase que representa toda la aplicacion de la calculadora.
    """

    def __init__(self, argv: list) -> None:
        super().__init__(argv)

        # Se instancian los compoentnes del MVC de la calculadora
        self.model = CalculatorModel()
        self.controller = CalculatorController(self.model)
        self.view = CalculatorView(self.model, self.controller)

        # Se inicia mostrando la vista
        self.view.show()


# Comprobacion inicial que se da si el archivo main.py
# se llama desde una terminal a modo de modulo
if __name__ == "__main__":
    # Se instancia una nueva Calculadora
    app = Calculator(sys.argv)
    sys.exit(app.exec_())
