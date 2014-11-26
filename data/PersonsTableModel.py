# -*- coding: utf-8 -*-

__author__ = 'Juan Manuel Bermúdez Cabrera'

from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex


class PersonsTableModel(QAbstractTableModel):

    def __init__(self, patients=[]):
        QAbstractTableModel.__init__(self)
        self.patients = patients
        self.__column_to_name = {0:'nombre', 1:'edad', 2:'provincia'}

    def rowCount(self, model_index=QModelIndex()):
        return len(self.patients)

    def columnCount(self, model_index = QModelIndex()):
        return 3

    def data(self, model_index=QModelIndex(), role=Qt.DisplayRole):
        if role == Qt.DisplayRole and model_index.isValid():
            patient = self.patients[model_index.row()]
            col = model_index.column()

            if col != 2:
                return getattr(patient, self.__column_to_name[col])
            return patient.provincia.nombre

        if role == Qt.UserRole:
            return self.patients[model_index.row()].id

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.__column_to_name[section].capitalize()
        return None
