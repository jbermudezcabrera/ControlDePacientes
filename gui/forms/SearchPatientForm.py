# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QDialog

from gui.forms.PatientForm import PatientForm
from data.PersonsTableModel import PersonsTableModel

class SearchPatientForm(QWidget):
    def __init__(self, controller, *args):
        super(SearchPatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'SearchPatientForm.ui'), self)

        self.controller = controller

        self.searchBtn.clicked.connect(self.on_search_clicked)
        self.modifyBtn.clicked.connect(self.on_modify_clicked)

    @pyqtSlot()
    def on_search_clicked(self):
        patients = self.controller.find_patients(self.queryInput.text().strip())
        model = PersonsTableModel(patients)
        self.patientsTable.setModel(model)

    @pyqtSlot()
    def on_modify_clicked(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle('Modificar paciente')

        form = PatientForm(self.controller)
        form.setParent(dialog)

        # TODO: pass selected patient if any
        form.modify_patient(None)

        dialog.show()
