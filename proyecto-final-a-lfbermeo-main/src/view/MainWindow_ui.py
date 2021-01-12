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
        self.sldAverageDays = QtWidgets.QSlider(self.grpControls)
        self.sldAverageDays.setGeometry(QtCore.QRect(549, 40, 191, 22))
        self.sldAverageDays.setMinimum(1)
        self.sldAverageDays.setMaximum(15)
        self.sldAverageDays.setOrientation(QtCore.Qt.Horizontal)
        self.sldAverageDays.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sldAverageDays.setTickInterval(1)
        self.sldAverageDays.setObjectName("sldAverageDays")
        self.label_3 = QtWidgets.QLabel(self.grpControls)
        self.label_3.setGeometry(QtCore.QRect(490, 40, 47, 31))
        self.label_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.pnlOptions = QtWidgets.QGroupBox(self.grpControls)
        self.pnlOptions.setGeometry(QtCore.QRect(620, 79, 120, 141))
        self.pnlOptions.setObjectName("pnlOptions")
        self.rdbCumulative = QtWidgets.QRadioButton(self.pnlOptions)
        self.rdbCumulative.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rdbCumulative.setObjectName("rdbCumulative")
        self.rdbDaily = QtWidgets.QRadioButton(self.pnlOptions)
        self.rdbDaily.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rdbDaily.setObjectName("rdbDaily")
        self.pnlDataPlot = QtWidgets.QGroupBox(self.grpControls)
        self.pnlDataPlot.setGeometry(QtCore.QRect(490, 80, 120, 141))
        self.pnlDataPlot.setObjectName("pnlDataPlot")
        self.rdbCases = QtWidgets.QRadioButton(self.pnlDataPlot)
        self.rdbCases.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.rdbCases.setObjectName("rdbCases")
        self.rdbDeaths = QtWidgets.QRadioButton(self.pnlDataPlot)
        self.rdbDeaths.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.rdbDeaths.setObjectName("rdbDeaths")
        self.rdbBoth = QtWidgets.QRadioButton(self.pnlDataPlot)
        self.rdbBoth.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.rdbBoth.setObjectName("rdbBoth")
        self.pnlCuntry = QtWidgets.QGroupBox(self.grpControls)
        self.pnlCuntry.setGeometry(QtCore.QRect(20, 20, 211, 201))
        self.pnlCuntry.setObjectName("pnlCuntry")
        self.listCountries = QtWidgets.QListView(self.pnlCuntry)
        self.listCountries.setGeometry(QtCore.QRect(10, 20, 191, 171))
        self.listCountries.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listCountries.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listCountries.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.listCountries.setObjectName("listCountries")
        self.pnlState = QtWidgets.QGroupBox(self.grpControls)
        self.pnlState.setGeometry(QtCore.QRect(250, 20, 211, 201))
        self.pnlState.setObjectName("pnlState")
        self.listStates = QtWidgets.QListView(self.pnlState)
        self.listStates.setGeometry(QtCore.QRect(10, 20, 191, 171))
        self.listStates.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listStates.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listStates.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listStates.setObjectName("listStates")
        self.pnlPlot = QtWidgets.QFrame(self.centralwidget)
        self.pnlPlot.setGeometry(QtCore.QRect(20, 20, 761, 401))
        self.pnlPlot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pnlPlot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnlPlot.setObjectName("pnlPlot")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "COVID-19 Data Visualization (Data source: Johns Hopkins University)"))
        self.grpControls.setTitle(_translate("MainWindow", "Controles"))
        self.label_3.setText(_translate("MainWindow", "Average\n"
                                        "# of days"))
        self.pnlOptions.setTitle(_translate("MainWindow", "Option"))
        self.rdbCumulative.setText(_translate("MainWindow", "Cumulative"))
        self.rdbDaily.setText(_translate("MainWindow", "Daily"))
        self.pnlDataPlot.setTitle(_translate("MainWindow", "Data to plot"))
        self.rdbCases.setText(_translate("MainWindow", "Cases"))
        self.rdbDeaths.setText(_translate("MainWindow", "Deaths"))
        self.rdbBoth.setText(_translate("MainWindow", "Both"))
        self.pnlCuntry.setTitle(_translate("MainWindow", "Country"))
        self.pnlState.setTitle(_translate("MainWindow", "State or Region"))