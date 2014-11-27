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

        self.__init_table()

    def modify_tac(self, tac):
        self.__init_table()

        if tac is not None:
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

    def __init_table(self):
        types = self.controller.arteries
        row_count = len(types) + 1
        self.calcioScoreTable.setRowCount(row_count)

        for row in range(row_count - 1):
            artery_type = types[row]

            item = QTableWidgetItem(artery_type.nombre)
            item.setData(Qt.UserRole, artery_type.id)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.calcioScoreTable.setItem(row, 0, item)

        item = QTableWidgetItem('TOTAL')
        item.setData(Qt.UserRole, -1)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.calcioScoreTable.setItem(row_count - 1, 0, item)

        for column in range(1, self.calcioScoreTable.columnCount()):
            for row in range(self.calcioScoreTable.rowCount()):
                item = QTableWidgetItem()
                item.setText('0')

                if row == self.calcioScoreTable.rowCount() - 1:
                    item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.calcioScoreTable.setItem(row, column, item)
