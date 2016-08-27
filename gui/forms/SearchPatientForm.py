import os
from functools import partial

from PyQt4 import uic
from PyQt4.QtCore import Qt, pyqtSlot
from PyQt4.QtGui import QWidget, QDialog, QMessageBox

from gui import controller
from gui.forms.PatientForm import PatientForm
from data.PersonsTableModel import PersonsTableModel

__author__ = 'Juan Manuel Bermúdez Cabrera'


class SearchPatientForm(QWidget):
    def __init__(self, *args):
        super(SearchPatientForm, self).__init__(*args)

        uic.loadUi(os.path.join('resources', 'uis', 'SearchPatientForm.ui'), self)

        self.searchBtn.clicked.connect(self.on_search_clicked)
        self.modifyBtn.clicked.connect(self.on_modify_clicked)
        self.deleteBtn.clicked.connect(self.on_delete_clicked)
        self.patientsTable.doubleClicked.connect(self.on_modify_clicked)

        self.patientsTable.clicked.connect(partial(self.modifyBtn.setEnabled, True))
        self.patientsTable.clicked.connect(partial(self.deleteBtn.setEnabled, True))

    @pyqtSlot()
    def on_search_clicked(self):
        patients = controller.find_patients(self.queryInput.text().strip())
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

        patient = controller.patient(self._selected_patient_id())

        form = PatientForm()
        form.setParent(dialog)
        form.modify_patient(patient, dialog.close)

        dialog.exec()

    @pyqtSlot()
    def on_delete_clicked(self):
        reply = QMessageBox.question(self, 'Eliminar paciente',
                                     '¿Desea eliminar el paciente seleccionado?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            controller.delete_patient(self._selected_patient_id())
            self.on_search_clicked()

    def _selected_patient_id(self):
        index_model = self.patientsTable.selectedIndexes()[0]
        patient_id = self.patientsTable.model().data(index_model, Qt.UserRole)
        return patient_id
