#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from src.model.M_MainWindow import MainModel
from src.controller.C_MainWindow import MainController
from src.view.V_MainWindow import MainView


class App(QApplication):
    def __init__(self, argv: list) -> None:
        super().__init__(argv)

        self.model = MainModel()
        self.controller = MainController(self.model)
        self.view = MainView(self.model, self.controller)
        self.view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())
