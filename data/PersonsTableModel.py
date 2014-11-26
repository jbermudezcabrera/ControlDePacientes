# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex

PROVINCE_COLUMN = 2

class PersonsTableModel(QAbstractTableModel):

    def __init__(self, patients=[]):
        QAbstractTableModel.__init__(self)
        self.patients = patients
        self.__column_to_name = {0:'nombre', 1:'edad',
                                 PROVINCE_COLUMN:'provincia'}

    def rowCount(self, model_index=QModelIndex()):
        return len(self.patients)

    def columnCount(self, model_index = QModelIndex()):
        return 3

    def data(self, model_index=QModelIndex(), role=Qt.DisplayRole):
        if role == Qt.DisplayRole and model_index.isValid():
            patient = self.patients[model_index.row()]
            col = model_index.column()

            if col != PROVINCE_COLUMN:
                return getattr(patient, self.__column_to_name[col])
            return patient.provincia.nombre

        if role == Qt.UserRole:
            return self.patients[model_index.row()].id

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.__column_to_name[section].capitalize()
        return None

    def sort(self, column, order=Qt.AscendingOrder):
        column_name = self.__column_to_name[column]
        reverse = order == Qt.DescendingOrder

        self.layoutAboutToBeChanged.emit()

        if column != PROVINCE_COLUMN:
            self.patients.sort(key=lambda p: getattr(p, column_name),
                               reverse=reverse)
        else:
            self.patients.sort(key=lambda p: p.provincia.nombre,
                               reverse=reverse)

        ifrom = self.createIndex(0, 0)
        ito = self.createIndex(len(self.patients),len(self.__column_to_name))

        self.changePersistentIndex(ifrom, ito)
        self.layoutChanged.emit()
