# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sys

from PyQt5.uic import loadUi

import PyQt5.QtCore as core
import PyQt5.QtWidgets as gui

from PatientForm import PatientForm


class MainWindow(gui.QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'MainWindow.ui'), self)
        #compileUi(os.path.join('resources', 'uis', 'MainWindow.ui'), open('test.py', 'w'))

        self.addPatientAction.triggered.connect(self.on_add_patient)

    @core.pyqtSlot()
    def on_add_patient(self):
        PatientForm(self.centralwidget)


app = gui.QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())
