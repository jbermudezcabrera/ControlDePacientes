# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot, QRegExp, Qt
from PyQt5.QtGui import QValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QMessageBox

from gui.forms.APPDialog import APPDialog
from gui.forms.TACDialog import TACDialog
from gui.forms.ACDialog import ACDialog


class CIValidator(QValidator):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__regexp = CIValidator.regexp(self)

    def validate(self, value, pos):
        state = self.__regexp.validate(value, pos)

        if state[0] == QValidator.Acceptable:
            if not self.controller.find_patients(value):
                return QValidator.Acceptable, state[1], state[2]
            return QValidator.Invalid, state[1], state[2]

        return state

    @staticmethod
    def regexp(parent):
        return QRegExpValidator(QRegExp('\d{11,11}'), parent)

class PatientForm(QWidget):
    def __init__(self, controller, *args):
        super(PatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'PatientForm.ui'), self)

        self.patient = None
        self.controller = controller
        self.__input_to_sheet = {}
        self.__validator_to_input = {}

        self.__app_dialog = APPDialog(self.controller)
        self.__ac_dialog = ACDialog(self.controller)
        self.__tac_dialog = TACDialog(self.controller)

        self.__init_provinces()
        self.__init_validators()

        self.appBtn.clicked.connect(self.__app_dialog.show)
        self.acBtn.clicked.connect(self.__ac_dialog.show)
        self.tacBtn.clicked.connect(self.__tac_dialog.show)

        self.saveBtn.clicked.connect(self.on_save_clicked)

    def __init_provinces(self):
        for p in self.controller.provinces:
            self.provinceCombo.addItem(p.nombre, p.id)

    def __init_validators(self):
        regexp = QRegExpValidator(QRegExp('[a-z\s]+', Qt.CaseInsensitive), self)
        self.nameInput.setValidator(regexp)
        self.__validator_to_input[regexp] = self.nameInput

        civ = CIValidator(self.controller)
        self.ciInput.setValidator(civ)
        self.__validator_to_input[civ] = self.ciInput

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
            msg = 'No se ha podido cargar la provincia {}'
            self.show_error(msg=msg.format(patient.provincia.nombre))

        # change the concept of a valid CI, check only pattern correctness now
        self.__validator_to_input.pop(self.ciInput.validator())

        self.ciInput.setValidator(self.ciInput.validator().regexp(self))
        self.__validator_to_input[self.ciInput.validator()] = self.ciInput

        # modify form behaviour
        # cancel no longer closes form, now closes form's container
        self.cancelBtn.clicked.disconnect(self.close)
        self.cancelBtn.clicked.connect(lambda: self.parent().close())

        # make an update not an insert
        self.saveBtn.clicked.disconnect(self.on_save_clicked)
        self.saveBtn.clicked.connect(self.on_save_modified_clicked)

        # put app, ac and tac forms in modify mode
        self.__app_dialog.modify_app(self.patient.app)
        self.__ac_dialog.modify_ac(self.patient.complementario)

    @pyqtSlot()
    def on_save_clicked(self):
        if not self.validate_input():
            return

        # insert patient
        ci = self.ciInput.text().strip()
        name = self.nameInput.text().strip()
        age = self.ageInput.value()
        selected_prov_id = self.provinceCombo.currentData()

        try:
            patient_id = self.controller.add_patient(ci, name, age,
                                                     selected_prov_id)
        except Exception as ex:
            self.show_error(ex)
            return

        # insert patient APP
        if self.__app_dialog.data_collected:
            try:
                self.controller.set_patient_app(patient_id,
                                                self.__app_dialog.hta,
                                                self.__app_dialog.ci,
                                                self.__app_dialog.hc,
                                                self.__app_dialog.ht,
                                                self.__app_dialog.dm,
                                                self.__app_dialog.smoker,
                                                self.__app_dialog.other,
                                                self.__app_dialog.idiag)
            except Exception as ex:
                self.show_error(ex)
                return

        # insert patient AC
        if self.__ac_dialog.data_collected:
            try:
                self.controller.set_patient_ac(patient_id,
                                               self.__ac_dialog.hb,
                                               self.__ac_dialog.gli,
                                               self.__ac_dialog.crea,
                                               self.__ac_dialog.col,
                                               self.__ac_dialog.trig,
                                               self.__ac_dialog.au)
            except Exception as ex:
                self.show_error(ex)
                return

        QMessageBox.information(self, 'Información',
                                'Paciente registrado satisfactoriamente')
        self.close()

    @pyqtSlot()
    def on_save_modified_clicked(self):
        if not self.validate_input():
            return

        # collect APP data
        if self.__app_dialog.data_collected:
            hta = self.__app_dialog.hta
            ci = self.__app_dialog.ci
            hc = self.__app_dialog.hc
            ht = self.__app_dialog.ht
            dm = self.__app_dialog.dm
            smoker = self.__app_dialog.smoker
            other = self.__app_dialog.other
            idiag = self.__app_dialog.idiag

            if not self.patient.app:
                try:
                    self.controller.set_patient_app(self.patient.id, hta, ci,
                                                    hc, ht, dm, smoker, other,
                                                    idiag)
                except Exception as ex:
                    self.show_error(ex)
                    return
            else:
                # update APP
                app_id = self.patient.app.id

                try:
                    self.controller.update_app(app_id, hta, ci, hc, ht, dm,
                                               smoker, other, idiag)
                except Exception as ex:
                    self.show_error(ex)
                    return

        # collect AC data
        if self.__ac_dialog.data_collected:
            hb = self.__ac_dialog.hb
            gli = self.__ac_dialog.gli
            crea = self.__ac_dialog.crea
            col = self.__ac_dialog.col
            trig = self.__ac_dialog.trig
            au = self.__ac_dialog.au

            if not self.patient.complementario:
                try:
                    self.controller.set_patient_ac(self.patient.id, hb, gli,
                                                   crea, col, trig, au)
                except Exception as ex:
                    self.show_error(ex)
                    return
            else:
                # update AC
                ac_id = self.patient.complementario.id

                try:
                    self.controller.update_ac(ac_id, hb, gli, crea, col,
                                              trig, au)
                except Exception as ex:
                    self.show_error(ex)
                    return

        # collect patient data
        ci = self.ciInput.text().strip()
        name = self.nameInput.text().strip()
        age = self.ageInput.value()
        selected_prov_id = self.provinceCombo.currentData()

        # update patient
        try:
            self.controller.update_patient(self.patient.id, ci, name, age,
                                           selected_prov_id)
            QMessageBox.information(self, 'Información',
                                    'Paciente actualizado correctamente')
            self.parent().close()
        except Exception as ex:
            self.show_error(ex)

    def validate_input(self):
        valid = True

        for v, i in self.__validator_to_input.items():
            if v.validate(i.text(), len(i.text()))[0] != QValidator.Acceptable:
                valid = False
                self.__input_to_sheet[i] = i.styleSheet()
                i.setStyleSheet('border: 1px solid red')
            elif i in self.__input_to_sheet:
                i.setStyleSheet(self.__input_to_sheet[i])

        if not valid:
            QMessageBox.warning(self, 'Valores incorrectos',
                                'Algunos campos contienen información inválida')
        return valid

    def show_error(self, error='', title='Error',
                   msg='Ha ocurrido el siguiente error:\n'):
        text = msg + str(error)
        QMessageBox.critical(self, title, text)
