# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox


class ACDialog(QDialog):
    def __init__(self, controller, *args):
        super(ACDialog, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'ACDialog.ui'), self)

        self.controller = controller

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)

        self.hb = None
        self.gli = None
        self.crea = None
        self.col = None
        self.trig = None
        self.au = None

        self.__data_collected = False

    def modify_ac(self, ac):
        if ac is not None:
            self.hbInput.setValue(ac.hb)
            self.gliInput.setValue(ac.glicemia)
            self.creaInput.setValue(ac.creatinina)
            self.colInput.setValue(ac.colesterol)
            self.trigInput.setValue(ac.trigliceridos)
            self.acidInput.setValue(ac.acido_urico)

    @property
    def data_collected(self):
        return self.__data_collected

    @pyqtSlot()
    def on_save(self):
        self.hb = self.hbInput.value()
        self.gli = self.gliInput.value()
        self.crea = self.creaInput.value()
        self.col = self.colInput.value()
        self.trig = self.trigInput.value()
        self.au = self.acidInput.value()

        self.__data_collected = True
        self.close()
