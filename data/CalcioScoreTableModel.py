# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex

ARTERY_COLUMN = 0

class CalcioScoreTableModel(QAbstractTableModel):

    def __init__(self, arteries=[]):
        QAbstractTableModel.__init__(self)
        self.arteries = arteries
        self.__index_to_field_name = {ARTERY_COLUMN:'tipo', 1:'lesiones',
                                      2:'volumen', 3:'masa', 4:'calcio'}
        self.__index_to_column_name = {ARTERY_COLUMN:'Arteria', 1:'Nº Lesiones',
                                       2:'Volumen', 3:'Masa Eq.',
                                       4:'Cuantificación de calcio'}

    def rowCount(self, model_index=QModelIndex()):
        # add Totals row only if there are arteries
        return len(self.arteries) + 1 if self.arteries else 0

    def columnCount(self, model_index = QModelIndex()):
        return len(self.__index_to_column_name)

    def data(self, model_index=QModelIndex(), role=Qt.DisplayRole):
        if role == Qt.DisplayRole and model_index.isValid():
            row = model_index.row()
            col = model_index.column()

            # is the Total row?
            if row == self.rowCount():
                if col == ARTERY_COLUMN:
                    return 'Total'
                return self.__get_total(col)

            artery = self.arteries[row]

            if col != ARTERY_COLUMN:
                return getattr(artery, self.__index_to_field_name[col])
            return artery.tipo.nombre

        if role == Qt.UserRole:
            return self.arteries[model_index.row()].id

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.__index_to_column_name[section]

        return None

    def sort(self, column, order=Qt.AscendingOrder):
        column_name = self.__index_to_field_name[column]
        reverse = order == Qt.DescendingOrder

        self.layoutAboutToBeChanged.emit()

        if column != ARTERY_COLUMN:
            self.arteries.sort(key=lambda p: getattr(p, column_name),
                               reverse=reverse)
        else:
            self.arteries.sort(key=lambda a: a.tipo.nombre, reverse=reverse)

        ifrom = self.createIndex(0, 0)
        ito = self.createIndex(len(self.arteries),len(self.__index_to_field_name))

        self.changePersistentIndex(ifrom, ito)
        self.layoutChanged.emit()

    def __get_total(self, column):
        field_name = self.__index_to_field_name[column]
        column_values = map(lambda artery: getattr(artery, field_name))
        return sum(column_values)
