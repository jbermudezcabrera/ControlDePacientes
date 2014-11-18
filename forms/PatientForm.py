# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QDialog

from forms.APPForm import APPForm
from forms.ACForm import ACForm
from forms.TACForm import TACForm


class PatientForm(QWidget):
    def __init__(self, *args):
        super(PatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'PatientForm.ui'), self)

        self.appBtn.clicked.connect(self.on_app_btn_clicked)
        self.acBtn.clicked.connect(self.on_ac_btn_clicked)
        self.tacBtn.clicked.connect(self.on_tac_btn_clicked)

        self.__app_dialog = APPForm()
        self.__ac_dialog = ACForm()
        self.__tac_dialog = TACForm()

    @pyqtSlot()
    def on_app_btn_clicked(self):
        self.__app_dialog.show()

    @pyqtSlot()
    def on_ac_btn_clicked(self):
        self.__ac_dialog.show()

    @pyqtSlot()
    def on_tac_btn_clicked(self):
        self.__tac_dialog.show()
