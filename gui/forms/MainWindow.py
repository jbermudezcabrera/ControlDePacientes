import os

from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow

from gui.forms.PatientForm import PatientForm
from gui.forms.SearchPatientForm import SearchPatientForm

__author__ = 'Juan Manuel Bermúdez Cabrera'


class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        uic.loadUi(os.path.join('resources', 'uis', 'MainWindow.ui'), self)

        self.addPatientAction.triggered.connect(self.on_add_patient)
        self.searchAction.triggered.connect(self.on_search_patient)

        self.searchAction.trigger()

    @pyqtSlot()
    def on_add_patient(self):
        central = self.centralWidget()

        if not (isinstance(central, PatientForm) and central.isVisible()):
            self.setCentralWidget(PatientForm())

    @pyqtSlot()
    def on_search_patient(self):
        central = self.centralWidget()

        if not isinstance(central, SearchPatientForm) or not central.isVisible():
            self.setCentralWidget(SearchPatientForm())
