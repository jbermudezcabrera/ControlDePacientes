# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

import os.path
from datetime import date

from PyQt5.uic import loadUi

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem

from data.CalcioScoreTableModel import CalcioScoreTableModel


class TACDialog(QDialog):
    def __init__(self, controller, *args):
        super(TACDialog, self).__init__(*args)

        loadUi(os.path.join('resources', 'uis', 'TACDialog.ui'), self)

        self.controller = controller
        self.__data_collected = False

        self.date = date.today()
        self.angio = None

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)
        self.dateInput.setDate(self.date)   # set today's date

        self.__fill_table()

    def modify_tac(self, tac):
        if tac is not None:
            self.__fill_table(tac.arterias)
            # TODO: restore tac data
            pass

    @property
    def data_collected(self):
        return self.__data_collected

    @pyqtSlot()
    def on_save(self):
        qdate = self.dateInput.date()
        self.date = self.date.replace(qdate.year(), qdate.month(), qdate.day())
        self.angio = self.angioInput.toPlainText().strip()

        # TODO: save data
        self.__data_collected = True
        self.close()

    def __fill_table(self, arteries=[]):
        row_count = self.calcioScoreTable.rowCount()

        # mark arteries column as non editable
        for row in range(row_count):
            item = self.calcioScoreTable.item(row, 0)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        # mark totals row as non editable
        row_count -=1
        for column in range(self.calcioScoreTable.columnCount()):
            item = self.calcioScoreTable.item(row_count, column)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        if arteries:
            pass
