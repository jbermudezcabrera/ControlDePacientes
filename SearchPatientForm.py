# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget


class SearchPatientForm(QWidget):
    def __init__(self, *args):
        super(SearchPatientForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'SearchPatientForm.ui'), self)
