# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
import sys

from PyQt5.uic import loadUi

import PyQt5.QtCore as core
import PyQt5.QtWidgets as gui

from forms.PatientForm import PatientForm
from forms.SearchPatientForm import SearchPatientForm


class MainWindow(gui.QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'MainWindow.ui'), self)
        #compileUi(os.path.join('resources', 'uis', 'MainWindow.ui'),
        # open('test.py', 'w'))

        self.addPatientAction.triggered.connect(self.on_add_patient)
        self.searchAction.triggered.connect(self.on_search_patient)

    @core.pyqtSlot()
    def on_add_patient(self):
        self.setCentralWidget(PatientForm())

    @core.pyqtSlot()
    def on_search_patient(self):
        self.setCentralWidget(SearchPatientForm())


app = gui.QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())
