#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from src.model import CalculatorModel
from src.controller import CalculatorController
from src.view import CalculatorView


class Calculator(QApplication):
    def __init__(self, argv: list) -> None:
        super().__init__(argv)

        self.model = CalculatorModel()
        self.controller = CalculatorController(self.model)
        self.view = CalculatorView(self.model, self.controller)

        self.view.show()


if __name__ == "__main__":
    app = Calculator(sys.argv)
    sys.exit(app.exec_())
