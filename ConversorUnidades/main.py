#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from src.controller import ConversorController
from src.model import ConversorModel
from src.view import ConversorView


class Conversor(QApplication):
    """
    Calse que representa toda la aplicacion del conversor.
    """

    def __init__(self, argv: list) -> None:
        super().__init__(argv)

        self.model = ConversorModel()
        self.controller = ConversorController(self.model)
        self.view = ConversorView(self.model, self.controller)

        self.view.show()


if __name__ == "__main__":
    app = Conversor(sys.argv)
    sys.exit(app.exec_())
