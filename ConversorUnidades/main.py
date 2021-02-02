#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication


class Conversor(QApplication):
    """
    Calse que representa toda la aplicacion del conversor.
    """

    def __init__(self, argv: list) -> None:
        super().__init__(argv)


if __name__ == "__main__":
    app = Conversor(sys.argv)
    sys.exit(app.exec_())
