from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from src.view_ui import Ui_MainWindow
from src.model import CalculatorModel
from src.controller import CalculatorController


class CalculatorView(QMainWindow):
    """
    Clase que representa la interfaz grafica de la calculadora
    """

    def __init__(self, model: CalculatorModel, controller: CalculatorController) -> None:
        """
        Constructor
        """
        super().__init__()
        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()

        self._ui.setupUi(self)

        self.connectWithController()
        self.connectWithModel()

    def connectWithController(self):
        """
        Metodo en el cual se conectan todos los eventos de la interfaz con sus respectivos controladores
        """
        # Escribe nuevos tokens numeros
        self._ui.btn0.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn0.text()))
        self._ui.btn1.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn1.text()))
        self._ui.btn2.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn2.text()))
        self._ui.btn3.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn3.text()))
        self._ui.btn4.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn4.text()))
        self._ui.btn5.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn5.text()))
        self._ui.btn6.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn6.text()))
        self._ui.btn7.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn7.text()))
        self._ui.btn8.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn8.text()))
        self._ui.btn9.clicked.connect(
            lambda: self._controller.addToken(self._ui.btn9.text()))

        # Escribe nuevos tokens operadores
        self._ui.btnDivision.clicked.connect(
            lambda: self._controller.addToken(self._ui.btnDivision.text()))
        self._ui.btnMultiply.clicked.connect(
            lambda: self._controller.addToken(self._ui.btnMultiply.text()))
        self._ui.btnSubstract.clicked.connect(
            lambda: self._controller.addToken(self._ui.btnSubstract.text()))
        self._ui.btnAdd.clicked.connect(
            lambda: self._controller.addToken(self._ui.btnAdd.text()))
        self._ui.btnDot.clicked.connect(
            lambda: self._controller.addToken(self._ui.btnDot.text()))

        # Borra tokens
        self._ui.btnClear.clicked.connect(self._controller.clear)
        self._ui.btnClearAll.clicked.connect(self._controller.clearAll)

        # Resuelve la operacion
        self._ui.btnEquals.clicked.connect(self._controller.resolve)

    def connectWithModel(self):
        """
        Metodo en el cual se conectan todos los cambios del modelo con la interfaz
        """
        self._model.expressionChanged.connect(self.onResultValueChanged)

    @pyqtSlot(str)
    def onResultValueChanged(self, value):
        """
        Metodo que se ejecuta al escuchar un cambio en el valor del modelo
        """
        self._ui.display.setText(value)
