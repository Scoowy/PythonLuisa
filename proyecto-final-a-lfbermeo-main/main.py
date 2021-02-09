#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from src.model.M_MainWindow import MainModel
from src.controller.C_MainWindow import MainController
from src.view.V_MainWindow import MainView


class App(QApplication):
    """
    Clase pricipal que representa la aplicacion principal
    """

    def __init__(self, argv: list) -> None:
        """
        Constructor
        """
        super().__init__(argv)

        # Instanciamos y pasamos las refernecias armando el patron MVC
        self.model = MainModel()
        self.controller = MainController(self.model)
        self.view = MainView(self.model, self.controller)

        # Presentamos la ventana principal
        self.view.show()


if __name__ == "__main__":
    """
    Condicional que se ejecutara si este archivo es ejecutado directamente
    """
    # Instanciamos una nueva la clase App
    app = App(sys.argv)
    # Le pasamos el control de terminar la ejecucion una vez se cierre la ventana
    sys.exit(app.exec_())
