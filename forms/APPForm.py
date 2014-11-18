# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog


class APPForm(QDialog):
    def __init__(self, *args):
        super(APPForm, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'APPForm.ui'), self)
