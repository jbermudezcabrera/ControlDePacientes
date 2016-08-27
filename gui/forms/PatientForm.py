import os

from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot, QRegExp, Qt
from PyQt4.QtGui import QValidator, QRegExpValidator, QWidget, QMessageBox

from gui import controller
from gui.forms.APPDialog import APPDialog
from gui.forms.TACDialog import TACDialog
from gui.forms.ACDialog import ACDialog

__author__ = 'Juan Manuel Bermúdez Cabrera'


class PatientForm(QWidget):
    def __init__(self, *args):
        super(PatientForm, self).__init__(*args)

        uic.loadUi(os.path.join('resources', 'uis', 'PatientForm.ui'), self)

        self.patient = None
        self._input_to_sheet = {}
        self._validator_to_input = {}

        self._app_dialog = APPDialog()
        self._ac_dialog = ACDialog()
        self._tac_dialog = TACDialog()

        self._init_provinces()
        self._init_validators()

        self.appBtn.clicked.connect(self._app_dialog.show)
        self.acBtn.clicked.connect(self._ac_dialog.show)
        self.tacBtn.clicked.connect(self._tac_dialog.show)

        self.saveBtn.clicked.connect(self.on_save_clicked)

    def _init_provinces(self):
        for p in controller.provinces():
            self.provinceCombo.addItem(p.nombre, p.id)

    def _init_validators(self):
        regexp = QRegExpValidator(QRegExp('[a-záéíóú\s]+', Qt.CaseInsensitive), self)
        self.nameInput.setValidator(regexp)
        self._validator_to_input[regexp] = self.nameInput

        civ = QRegExpValidator(QRegExp('\d{11,11}'), self)
        self.ciInput.setValidator(civ)
        self._validator_to_input[civ] = self.ciInput

    def modify_patient(self, patient, cancel_cb):
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

        # callback invoked when cancel button is pressed
        self.cancelBtn.clicked.connect(cancel_cb)

        # make an update not an insert
        self.saveBtn.clicked.disconnect(self.on_save_clicked)
        self.saveBtn.clicked.connect(self.on_save_modified_clicked)

        # put app, ac and tac forms in modify mode
        self._app_dialog.modify_app(self.patient.app)
        self._ac_dialog.modify_ac(self.patient.complementario)
        self._tac_dialog.modify_tac(self.patient.tac)

    @pyqtSlot()
    def on_save_clicked(self):
        if not self.validate_input():
            return

        # insert patient
        ci = self.ciInput.text().strip()
        name = self.nameInput.text().strip()
        age = self.ageInput.value()
        selected_prov_id = self.provinceCombo.itemData(self.provinceCombo.currentIndex())

        try:
            patient_id = controller.add_patient(ci, name, age, selected_prov_id)
        except Exception as ex:
            self.show_error(ex)
            return

        # insert patient APP
        if self._app_dialog.data_collected:
            try:
                controller.set_patient_app(patient_id,
                                           self._app_dialog.hta,
                                           self._app_dialog.ci,
                                           self._app_dialog.hc,
                                           self._app_dialog.ht,
                                           self._app_dialog.dm,
                                           self._app_dialog.smoker,
                                           self._app_dialog.other,
                                           self._app_dialog.idiag)
            except Exception as ex:
                self.show_error(ex)
                return

        # insert patient AC
        if self._ac_dialog.data_collected:
            try:
                controller.set_patient_ac(patient_id,
                                          self._ac_dialog.hb,
                                          self._ac_dialog.gli,
                                          self._ac_dialog.crea,
                                          self._ac_dialog.col,
                                          self._ac_dialog.trig,
                                          self._ac_dialog.au)
            except Exception as ex:
                self.show_error(ex)
                return

        if self._tac_dialog.data_collected:
            try:
                controller.set_patient_tac(patient_id,
                                           self._tac_dialog.date,
                                           self._tac_dialog.angio,
                                           self._tac_dialog.artery_to_data)
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
        if self._app_dialog.data_collected:
            hta = self._app_dialog.hta
            ci = self._app_dialog.ci
            hc = self._app_dialog.hc
            ht = self._app_dialog.ht
            dm = self._app_dialog.dm
            smoker = self._app_dialog.smoker
            other = self._app_dialog.other
            idiag = self._app_dialog.idiag

            if not self.patient.app:
                try:
                    controller.set_patient_app(self.patient.id, hta, ci,
                                               hc, ht, dm, smoker, other,
                                               idiag)
                except Exception as ex:
                    self.show_error(ex)
                    return
            else:
                # update APP
                app_id = self.patient.app.id

                try:
                    controller.update_app(app_id, hta, ci, hc, ht, dm,
                                          smoker, other, idiag)
                except Exception as ex:
                    self.show_error(ex)
                    return

        # collect AC data
        if self._ac_dialog.data_collected:
            hb = self._ac_dialog.hb
            gli = self._ac_dialog.gli
            crea = self._ac_dialog.crea
            col = self._ac_dialog.col
            trig = self._ac_dialog.trig
            au = self._ac_dialog.au

            if not self.patient.complementario:
                try:
                    controller.set_patient_ac(self.patient.id, hb, gli,
                                              crea, col, trig, au)
                except Exception as ex:
                    self.show_error(ex)
                    return
            else:
                # update AC
                ac_id = self.patient.complementario.id

                try:
                    controller.update_ac(ac_id, hb, gli, crea, col,
                                         trig, au)
                except Exception as ex:
                    self.show_error(ex)
                    return

        # collect TAC data
        if self._tac_dialog.data_collected:
            date = self._tac_dialog.date
            angio = self._tac_dialog.angio
            arteries = self._tac_dialog.artery_to_data

            if not self.patient.tac:
                try:
                    controller.set_patient_tac(self.patient.id, date,
                                               angio, arteries)
                except Exception as ex:
                    self.show_error(ex)
                    return
            else:
                # update TAC
                tac_id = self.patient.tac.id

                try:
                    controller.update_tac(tac_id, date, angio, arteries)
                except Exception as ex:
                    self.show_error(ex)
                    return

        # collect patient data
        ci = self.ciInput.text().strip()
        name = self.nameInput.text().strip()
        age = self.ageInput.value()
        selected_prov_id = self.provinceCombo.itemData(self.provinceCombo.currentIndex())

        # update patient
        try:
            controller.update_patient(self.patient.id, ci, name, age,
                                      selected_prov_id)
            QMessageBox.information(self, 'Información',
                                    'Paciente actualizado correctamente')
            self.parent().close()
        except Exception as ex:
            self.show_error(ex)

    def validate_input(self):
        valid = True

        for v, i in self._validator_to_input.items():
            if v.validate(i.text(), len(i.text()))[0] != QValidator.Acceptable:
                valid = False
                self._input_to_sheet[i] = i.styleSheet()
                i.setStyleSheet('border: 1px solid red')
            elif i in self._input_to_sheet:
                i.setStyleSheet(self._input_to_sheet[i])

        if not valid:
            QMessageBox.warning(self, 'Valores incorrectos',
                                'Algunos campos contienen información inválida')
        return valid

    def show_error(self, error=None, title='Error',
                   msg='Ha ocurrido el siguiente error:\n\n'):
        text = msg + (str(error) if error else '')
        QMessageBox.critical(self, title, text)
