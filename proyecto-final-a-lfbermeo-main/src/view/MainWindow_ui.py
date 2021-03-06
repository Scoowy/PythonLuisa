# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpControls = QtWidgets.QGroupBox(self.centralwidget)
        self.grpControls.setGeometry(QtCore.QRect(20, 440, 761, 241))
        self.grpControls.setObjectName("grpControls")
        self.pnlOptions = QtWidgets.QGroupBox(self.grpControls)
        self.pnlOptions.setGeometry(QtCore.QRect(620, 99, 120, 121))
        self.pnlOptions.setObjectName("pnlOptions")
        self.rdbCumulative = QtWidgets.QRadioButton(self.pnlOptions)
        self.rdbCumulative.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rdbCumulative.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rdbCumulative.setChecked(True)
        self.rdbCumulative.setObjectName("rdbCumulative")
        self.rdbDaily = QtWidgets.QRadioButton(self.pnlOptions)
        self.rdbDaily.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rdbDaily.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rdbDaily.setObjectName("rdbDaily")
        self.pnlDataPlot = QtWidgets.QGroupBox(self.grpControls)
        self.pnlDataPlot.setGeometry(QtCore.QRect(480, 100, 120, 121))
        self.pnlDataPlot.setObjectName("pnlDataPlot")
        self.rdbCases = QtWidgets.QRadioButton(self.pnlDataPlot)
        self.rdbCases.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rdbCases.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rdbCases.setObjectName("rdbCases")
        self.rdbDeaths = QtWidgets.QRadioButton(self.pnlDataPlot)
        self.rdbDeaths.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rdbDeaths.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rdbDeaths.setObjectName("rdbDeaths")
        self.rdbBoth = QtWidgets.QRadioButton(self.pnlDataPlot)
        self.rdbBoth.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.rdbBoth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rdbBoth.setChecked(True)
        self.rdbBoth.setObjectName("rdbBoth")
        self.pnlCuntry = QtWidgets.QGroupBox(self.grpControls)
        self.pnlCuntry.setGeometry(QtCore.QRect(20, 20, 211, 201))
        self.pnlCuntry.setObjectName("pnlCuntry")
        self.listCountries = QtWidgets.QListWidget(self.pnlCuntry)
        self.listCountries.setGeometry(QtCore.QRect(10, 20, 191, 171))
        self.listCountries.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listCountries.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listCountries.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listCountries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listCountries.setObjectName("listCountries")
        self.pnlState = QtWidgets.QGroupBox(self.grpControls)
        self.pnlState.setGeometry(QtCore.QRect(250, 20, 211, 201))
        self.pnlState.setObjectName("pnlState")
        self.listStates = QtWidgets.QListWidget(self.pnlState)
        self.listStates.setGeometry(QtCore.QRect(10, 20, 191, 171))
        self.listStates.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listStates.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listStates.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listStates.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listStates.setObjectName("listStates")
        self.groupBox = QtWidgets.QGroupBox(self.grpControls)
        self.groupBox.setGeometry(QtCore.QRect(480, 20, 261, 71))
        self.groupBox.setObjectName("groupBox")
        self.sldAverageDays = QtWidgets.QSlider(self.groupBox)
        self.sldAverageDays.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.sldAverageDays.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sldAverageDays.setMinimum(1)
        self.sldAverageDays.setMaximum(15)
        self.sldAverageDays.setPageStep(1)
        self.sldAverageDays.setOrientation(QtCore.Qt.Horizontal)
        self.sldAverageDays.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sldAverageDays.setTickInterval(1)
        self.sldAverageDays.setObjectName("sldAverageDays")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 16, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lcdRange = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdRange.setGeometry(QtCore.QRect(210, 20, 41, 41))
        self.lcdRange.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdRange.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdRange.setDigitCount(2)
        self.lcdRange.setObjectName("lcdRange")
        self.pnlPlot = PlotWidget(self.centralwidget)
        self.pnlPlot.setGeometry(QtCore.QRect(20, 20, 761, 401))
        self.pnlPlot.setObjectName("pnlPlot")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVID-19 Data Visualization (Data source: Johns Hopkins University)"))
        self.grpControls.setTitle(_translate("MainWindow", "Controles"))
        self.pnlOptions.setTitle(_translate("MainWindow", "Option"))
        self.rdbCumulative.setText(_translate("MainWindow", "Cumulative"))
        self.rdbDaily.setText(_translate("MainWindow", "Daily"))
        self.pnlDataPlot.setTitle(_translate("MainWindow", "Data to plot"))
        self.rdbCases.setText(_translate("MainWindow", "Cases"))
        self.rdbDeaths.setText(_translate("MainWindow", "Deaths"))
        self.rdbBoth.setText(_translate("MainWindow", "Both"))
        self.pnlCuntry.setTitle(_translate("MainWindow", "Country"))
        self.pnlState.setTitle(_translate("MainWindow", "State or Region"))
        self.groupBox.setTitle(_translate("MainWindow", "Average # of days"))
        self.label.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "15"))
from pyqtgraph import PlotWidget
