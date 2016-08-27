import os
from datetime import date

from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtGui import (QDialog, QDialogButtonBox, QTableWidgetItem, QSpinBox, QDoubleSpinBox,
                         QStyledItemDelegate)

__author__ = 'Juan Manuel Bermúdez Cabrera'


class TACDialog(QDialog):
    def __init__(self, controller, *args):
        super(TACDialog, self).__init__(*args)

        uic.loadUi(os.path.join('resources', 'uis', 'TACDialog.ui'), self)

        self.controller = controller
        self._data_collected = False

        self.date = date.today()
        self.angio = None
        self.artery_to_data = {}

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)
        self.dateInput.setDate(self.date)  # set today's date

        self._init_table()
        self.calcioScoreTable.cellChanged.connect(self.on_cell_changed)

    def modify_tac(self, tac):
        self._init_table()

        if tac is not None:
            self.dateInput.setDate(tac.fecha)
            self.angioInput.setPlainText(tac.angio_ct)
            self._fill_table(tac.arterias)
            pass

    @property
    def data_collected(self):
        return self._data_collected

    @pyqtSlot()
    def on_save(self):
        qdate = self.dateInput.date()
        self.date = self.date.replace(qdate.year(), qdate.month(), qdate.day())
        self.angio = self.angioInput.toPlainText().strip()

        for row in range(self.calcioScoreTable.rowCount() - 1):
            artery_id = self.calcioScoreTable.item(row, 0).data(Qt.UserRole)
            lessions = self.calcioScoreTable.item(row, 1).data(Qt.DisplayRole)
            volume = self.calcioScoreTable.item(row, 2).data(Qt.DisplayRole)
            mass = self.calcioScoreTable.item(row, 3).data(Qt.DisplayRole)
            calcium = self.calcioScoreTable.item(row, 4).data(Qt.DisplayRole)

            self.artery_to_data[artery_id] = lessions, volume, mass, calcium

        self._data_collected = True
        self.close()

    @pyqtSlot(int, int)
    def on_cell_changed(self, row, column):
        totals_row = self.calcioScoreTable.rowCount() - 1

        if column > 0 and row < totals_row:
            total = 0

            for r in range(totals_row):
                item = self.calcioScoreTable.item(r, column)
                total += item.data(Qt.DisplayRole)

            item = self.calcioScoreTable.item(totals_row, column)
            item.setData(Qt.DisplayRole, total)

    def _init_table(self):
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

        font = item.font()
        font.setBold(True)
        item.setFont(font)

        self.calcioScoreTable.setItem(row_count - 1, 0, item)

        for column in range(1, self.calcioScoreTable.columnCount()):
            for row in range(self.calcioScoreTable.rowCount()):
                item = QTableWidgetItem()
                item.setData(Qt.UserRole, 0)
                item.setData(Qt.DisplayRole, 0)

                # is Total's row?
                if row == self.calcioScoreTable.rowCount() - 1:
                    font = item.font()
                    font.setBold(True)

                    item.setFont(font)
                    item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.calcioScoreTable.setItem(row, column, item)

        # set item delegates for columns
        ## volumen, masa y calcio
        delegate = SpinBoxDelegate(self, True)
        self.calcioScoreTable.setItemDelegate(delegate)

        # lesiones
        int_delegate = SpinBoxDelegate(self, maximum=150)
        self.calcioScoreTable.setItemDelegateForColumn(1, int_delegate)

    def _fill_table(self, arteries):
        for artery in arteries:
            # find the corresponding row in the table
            for row in range(self.calcioScoreTable.rowCount()):
                artery_id = self.calcioScoreTable.item(row, 0).data(Qt.UserRole)

                # I find it
                if artery_id == artery.id:
                    # fill columns with artery data
                    item = self.calcioScoreTable.item(row, 1)
                    item.setData(Qt.DisplayRole, artery.lesiones)

                    item = self.calcioScoreTable.item(row, 2)
                    item.setData(Qt.DisplayRole, artery.volumen)

                    item = self.calcioScoreTable.item(row, 3)
                    item.setData(Qt.DisplayRole, artery.masa)

                    item = self.calcioScoreTable.item(row, 4)
                    item.setData(Qt.DisplayRole, artery.calcio)
                    break  # go to next artery


class SpinBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, double=False, minimum=0, maximum=10000):
        super(SpinBoxDelegate, self).__init__(parent)
        self.__double = double
        self.__min = minimum
        self.__max = maximum

    def createEditor(self, parent, option, index):
        editor = QDoubleSpinBox(parent) if self.__double else QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(self.__min)
        editor.setMaximum(self.__max)

        if self.__double:
            editor.setSingleStep(0.5)

        return editor

    def setEditorData(self, spin_box, index):
        value = index.model().data(index, Qt.EditRole)
        spin_box.setValue(value)

    def setModelData(self, spin_box, model, index):
        spin_box.interpretText()
        value = spin_box.value()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
