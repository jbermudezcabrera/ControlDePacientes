# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from gui.forms.APPDialog import APPDialog
from gui.forms.TACDialog import TACDialog
from gui.forms.ACDialog import ACDialog


class PatientForm(QWidget):
    def __init__(self, controller, *args):
        super(PatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'PatientForm.ui'), self)

        self.controller = controller

        self.appBtn.clicked.connect(self.on_app_btn_clicked)
        self.acBtn.clicked.connect(self.on_ac_btn_clicked)
        self.tacBtn.clicked.connect(self.on_tac_btn_clicked)

        self.__app_dialog = APPDialog(self.controller)
        self.__ac_dialog = ACDialog(self.controller)
        self.__tac_dialog = TACDialog(self.controller)

        self.__init_provinces()

    def __init_provinces(self):
        for ID, name in self.controller.provinces.items():
            self.provinceCombo.addItem(name, ID)

    @pyqtSlot()
    def on_app_btn_clicked(self):
        self.__app_dialog.show()

    @pyqtSlot()
    def on_ac_btn_clicked(self):
        self.__ac_dialog.show()

    @pyqtSlot()
    def on_tac_btn_clicked(self):
        self.__tac_dialog.show()
