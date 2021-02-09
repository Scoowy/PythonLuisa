# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\Calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 410)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 410))
        MainWindow.setMaximumSize(QtCore.QSize(350, 410))
        MainWindow.setStyleSheet("* {\n"
                                 "    color: rgb(42, 45, 52);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: rgb(191, 215, 234);\n"
                                 "    border-radius: 8;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(209, 226, 240);\n"
                                 "}\n"
                                 "\n"
                                 "#display {\n"
                                 "    border-radius: 8;\n"
                                 "    background-color: rgb(255, 251, 250);\n"
                                 "}\n"
                                 "\n"
                                 "#btnClear, #btnClearAll {\n"
                                 "    background-color: rgb(252, 107, 54);\n"
                                 "}\n"
                                 "\n"
                                 "#btnClear:hover, #btnClearAll:hover {\n"
                                 "    background-color: rgb(252, 122, 74);\n"
                                 "}\n"
                                 "\n"
                                 "#btnDivision, #btnMultiply, #btnSubstract, #btnAdd, #btnEquals, #btnDot {\n"
                                 "    background-color: rgb(255, 251, 250);\n"
                                 "}\n"
                                 "\n"
                                 "#btnDivision:hover, #btnMultiply:hover, #btnSubstract:hover, #btnAdd:hover, #btnEquals:hover, #btnDot:hover {\n"
                                 "    background-color: rgb(255, 239, 235);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(20, 20, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        font.setKerning(True)
        self.display.setFont(font)
        self.display.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.display.setReadOnly(True)
        self.display.setObjectName("display")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(100, 160, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(20, 160, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btnEquals = QtWidgets.QPushButton(self.centralwidget)
        self.btnEquals.setGeometry(QtCore.QRect(260, 280, 71, 111))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnEquals.setFont(font)
        self.btnEquals.setObjectName("btnEquals")
        self.btnDivision = QtWidgets.QPushButton(self.centralwidget)
        self.btnDivision.setGeometry(QtCore.QRect(180, 100, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnDivision.setFont(font)
        self.btnDivision.setObjectName("btnDivision")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(180, 160, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btnMultiply = QtWidgets.QPushButton(self.centralwidget)
        self.btnMultiply.setGeometry(QtCore.QRect(260, 100, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnMultiply.setFont(font)
        self.btnMultiply.setObjectName("btnMultiply")
        self.btnSubstract = QtWidgets.QPushButton(self.centralwidget)
        self.btnSubstract.setGeometry(QtCore.QRect(260, 160, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnSubstract.setFont(font)
        self.btnSubstract.setObjectName("btnSubstract")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(260, 220, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(180, 220, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(100, 220, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(20, 220, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(180, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(20, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(100, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(100, 340, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(180, 340, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnDot.setFont(font)
        self.btnDot.setObjectName("btnDot")
        self.btnClearAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearAll.setGeometry(QtCore.QRect(20, 100, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnClearAll.setFont(font)
        self.btnClearAll.setObjectName("btnClearAll")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(20, 340, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btnEquals.setText(_translate("MainWindow", "="))
        self.btnDivision.setText(_translate("MainWindow", "/"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnMultiply.setText(_translate("MainWindow", "*"))
        self.btnSubstract.setText(_translate("MainWindow", "-"))
        self.btnAdd.setText(_translate("MainWindow", "+"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnClearAll.setText(_translate("MainWindow", "AC"))
        self.btnClear.setText(_translate("MainWindow", "<x"))