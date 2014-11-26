# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox


class TACDialog(QDialog):
    def __init__(self, controller, *args):
        super(TACDialog, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'TACDialog.ui'), self)

        self.controller = controller
        self.__data_collected = False

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)

    def modify_tac(self, tac):
        if tac is not None:
            # TODO: restore tac data
            pass

    @property
    def data_collected(self):
        return self.__data_collected

    @pyqtSlot()
    def on_save(self):
        # TODO: save data
        self.__data_collected = True
        self.close()
