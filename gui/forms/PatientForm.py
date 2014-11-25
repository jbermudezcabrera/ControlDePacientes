# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from gui.forms.APPDialog import APPDialog
from gui.forms.TACDialog import TACDialog
from gui.forms.ACDialog import ACDialog


class PatientForm(QWidget):
    def __init__(self, controller, *args):
        super(PatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'PatientForm.ui'), self)

        self.controller = controller
        self.patient = None

        self.appBtn.clicked.connect(self.on_app_btn_clicked)
        self.acBtn.clicked.connect(self.on_ac_btn_clicked)
        self.tacBtn.clicked.connect(self.on_tac_btn_clicked)

        self.saveBtn.clicked.connect(self.on_save_clicked)

        self.__app_dialog = APPDialog(self.controller)
        self.__ac_dialog = ACDialog(self.controller)
        self.__tac_dialog = TACDialog(self.controller)

        self.__init_provinces()

    def __init_provinces(self):
        for p in self.controller.provinces:
            self.provinceCombo.addItem(p.nombre, p.id)

    def modify_patient(self, patient):
        self.patient = patient

        # fill input fields with patient data
        self.ciInput.setText(patient.ci)
        self.nameInput.setText(patient.nombre)
        self.ageInput.setValue(patient.edad)

        index = self.provinceCombo.findData(patient.provincia.id)

        if index >= 0:
           self.provinceCombo.setCurrentIndex(index)
        else:
            msg = 'No se ha podido cargar la provincia ' + patient.provincia.nombre
            QMessageBox.critical(self, 'Error', msg)

        # modify form behaviour
        # cancel no longer closes form, now closes form's container
        self.cancelBtn.clicked.disconnect(self.close)
        self.cancelBtn.clicked.connect(lambda: self.parent().close())

        # make an update not an insert
        self.saveBtn.clicked.disconnect(self.on_save_clicked)
        self.saveBtn.clicked.connect(self.on_save_modified_clicked)

        # put app, ac and tac forms in modify mode
        self.__app_dialog.modify_app(self.patient.app)

    @pyqtSlot()
    def on_app_btn_clicked(self):
        self.__app_dialog.show()

    @pyqtSlot()
    def on_ac_btn_clicked(self):
        self.__ac_dialog.show()

    @pyqtSlot()
    def on_tac_btn_clicked(self):
        self.__tac_dialog.show()

    @pyqtSlot()
    def on_save_clicked(self):
        ci = self.ciInput.text().strip()
        name = self.nameInput.text().strip()
        age = self.ageInput.value()
        selected_prov_id = self.provinceCombo.currentData()

        patient_id = self.controller.add_patient(ci, name, age, selected_prov_id)
        self.controller.set_patient_app(patient_id,
                                        self.__app_dialog.hta,
                                        self.__app_dialog.ci,
                                        self.__app_dialog.hc,
                                        self.__app_dialog.ht,
                                        self.__app_dialog.dm,
                                        self.__app_dialog.smoker,
                                        self.__app_dialog.other,
                                        self.__app_dialog.idiag)

        QMessageBox.information(self, 'Información',
                                'Paciente registrado satisfactoriamente')
        self.close()

    @pyqtSlot()
    def on_save_modified_clicked(self):
        # collect APP data
        app_id = self.patient.app.id
        hta = self.__app_dialog.hta
        ci = self.__app_dialog.ci
        hc = self.__app_dialog.hc
        ht = self.__app_dialog.ht
        dm = self.__app_dialog.dm
        smoker = self.__app_dialog.smoker
        other = self.__app_dialog.other
        idiag = self.__app_dialog.idiag

        # update APP
        self.controller.update_app(app_id, hta, ci, hc, ht, dm, smoker,
                                   other, idiag)

        # collect patient data
        ci = self.ciInput.text().strip()
        name = self.nameInput.text().strip()
        age = self.ageInput.value()
        selected_prov_id = self.provinceCombo.currentData()

        # update patient
        self.controller.update_patient(self.patient.id, ci, name, age,
                                       selected_prov_id)

        QMessageBox.information(self, 'Información',
                                'Paciente actualizado satisfactoriamente')
        self.parent().close()
