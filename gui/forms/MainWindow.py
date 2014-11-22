# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from gui.Controller import Controller
from gui.forms.PatientForm import PatientForm
from gui.forms.SearchPatientForm import SearchPatientForm

class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'MainWindow.ui'), self)
        #compileUi(os.path.join('resources', 'uis', 'PatientForm.ui'),
        #open('test.py', 'w'))

        self.controller = Controller()

        self.addPatientAction.triggered.connect(self.on_add_patient)
        self.searchAction.triggered.connect(self.on_search_patient)

    @pyqtSlot()
    def on_add_patient(self):
        self.setCentralWidget(PatientForm(self.controller))

    @pyqtSlot()
    def on_search_patient(self):
        self.setCentralWidget(SearchPatientForm(self.controller))
