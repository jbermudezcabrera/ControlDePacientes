# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget


class SearchPatientForm(QWidget):
    def __init__(self, controller, *args):
        super(SearchPatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'SearchPatientForm.ui'), self)

        self.controller = controller

        self.searchBtn.clicked.connect(self.on_search_clicked)

    def on_search_clicked(self):
        print(self.controller.find_patients(self.queryInput.text().strip()))
