# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\conversor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtIn = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIn.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.txtIn.setObjectName("txtIn")
        self.rdbMeters = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbMeters.setGeometry(QtCore.QRect(160, 40, 121, 17))
        self.rdbMeters.setChecked(True)
        self.rdbMeters.setObjectName("rdbMeters")
        self.rdbGrades = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbGrades.setGeometry(QtCore.QRect(160, 70, 121, 17))
        self.rdbGrades.setObjectName("rdbGrades")
        self.txtOut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOut.setGeometry(QtCore.QRect(310, 40, 113, 20))
        self.txtOut.setObjectName("txtOut")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Datos de entrada"))
        self.rdbMeters.setText(_translate(
            "MainWindow", "Metros a centimetros"))
        self.rdbGrades.setText(_translate(
            "MainWindow", "Celcius a Fahrenheit"))
        self.label_2.setText(_translate("MainWindow", "Opciones"))
        self.label_3.setText(_translate("MainWindow", "Datos de salida"))