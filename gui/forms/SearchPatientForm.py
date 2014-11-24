# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QDialog, QMessageBox

from gui.forms.PatientForm import PatientForm
from data.PersonsTableModel import PersonsTableModel


class SearchPatientForm(QWidget):
    def __init__(self, controller, *args):
        super(SearchPatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'SearchPatientForm.ui'), self)

        self.controller = controller

        self.searchBtn.clicked.connect(self.on_search_clicked)
        self.modifyBtn.clicked.connect(self.on_modify_clicked)
        self.deleteBtn.clicked.connect(self.on_delete_clicked)
        self.patientsTable.doubleClicked.connect(self.on_modify_clicked)

        self.patientsTable.clicked.connect(lambda: self.modifyBtn.setEnabled(True))
        self.patientsTable.clicked.connect(lambda: self.deleteBtn.setEnabled(True))

    @pyqtSlot()
    def on_search_clicked(self):
        patients = self.controller.find_patients(self.queryInput.text().strip())
        model = PersonsTableModel(patients)
        self.patientsTable.setModel(model)

        self.modifyBtn.setEnabled(False)
        self.deleteBtn.setEnabled(False)

    @pyqtSlot()
    def on_modify_clicked(self):
        dialog = QDialog(self)
        dialog.setModal(True)
        dialog.setWindowTitle('Modificar paciente')
        dialog.finished.connect(self.on_search_clicked)

        form = PatientForm(self.controller)
        form.setParent(dialog)
        form.modify_patient(self.controller.patient(self.__selected_patient_id()))

        dialog.show()

    @pyqtSlot()
    def on_delete_clicked(self):
        reply = QMessageBox.question(self, 'Eliminar paciente',
                                     '¿Desea eliminar el paciente seleccionado?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.controller.delete_patient(self.__selected_patient_id())
            self.on_search_clicked()

    def __selected_patient_id(self):
        index_model = self.patientsTable.selectedIndexes()[0]
        patient_id = self.patientsTable.model().data(index_model, Qt.UserRole)
        return patient_id
