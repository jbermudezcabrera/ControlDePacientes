# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from data.model import APP


class APPDialog(QDialog):
    def __init__(self, controller, *args):
        super(APPDialog, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'APPDialog.ui'), self)

        self.controller = controller
        self.app = None

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)

        self.hta = None
        self.ci = None
        self.hc = None
        self.ht = None
        self.dm = None
        self.smoker = None
        self.other = None
        self.idiag = None

        self.__init_dm()
        self.__init_smoker()

    def __init_dm(self):
        self.dmCombo.clear()
        self.dmCombo.addItem('No', 0)
        self.dmCombo.addItem('Tipo I', 1)
        self.dmCombo.addItem('Tipo II', 2)

    def __init_smoker(self):
        self.smokerCombo.clear()
        self.smokerCombo.addItem('No', 0)
        self.smokerCombo.addItem('Ex', 1)
        self.smokerCombo.addItem('Si', 2)

    def modify_app(self, app):
        self.app = app

        self.htaCheck.setChecked(app.hta)
        self.ciCheck.setChecked(app.ci)
        self.hclCheck.setChecked(app.hc)
        self.htdCheck.setChecked(app.ht)

        self.dmCombo.setCurrentIndex(self.dmCombo.fta(self.app.dm))
        self.smokerCombo.setCurrentIndex(self.smokerCombo.fta(self.app.fumador))

        self.otherInput.xt(self.app.otro)
        self.idInput.xt(self.app.idiagnostico)

    @pyqtSlot()
    def on_save(self):
        self.hta = self.htaCheck.isChecked()
        self.ci = self.ciCheck.isChecked()
        self.hc = self.hclCheck.isChecked()
        self.ht = self.htdCheck.isChecked()
        self.dm = self.dmCombo.currentData()
        self.smoker = self.smokerCombo.currentData()
        self.other = self.otherInput.text().strip()
        self.idiag = self.idInput.toPlainText().strip()
        self.close()
