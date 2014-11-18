# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\uis\MainWindow.ui'
#
# Created: Mon Nov 17 11:42:37 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(179, 79, 471, 381))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuPacientes = QtWidgets.QMenu(self.menubar)
        self.menuPacientes.setObjectName("menuPacientes")
        MainWindow.setMenuBar(self.menubar)
        self.add_patient_action = QtWidgets.QAction(MainWindow)
        self.add_patient_action.setObjectName("add_patient_action")
        self.menuPacientes.addAction(self.add_patient_action)
        self.menubar.addAction(self.menuPacientes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "teetetetetet"))
        self.menuPacientes.setTitle(_translate("MainWindow", "Pacientes"))
        self.add_patient_action.setText(_translate("MainWindow", "Agregar"))

