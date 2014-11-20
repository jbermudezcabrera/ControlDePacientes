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