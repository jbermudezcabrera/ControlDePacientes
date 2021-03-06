from PyQt4.QtCore import Qt, QAbstractTableModel, QModelIndex

__author__ = 'Juan Manuel Bermúdez Cabrera'

PROVINCE_COLUMN = 2


class PersonsTableModel(QAbstractTableModel):
    def __init__(self, patients=()):
        QAbstractTableModel.__init__(self)
        self.patients = patients
        self._index_to_field_name = {0: 'nombre', 1: 'edad',
                                     PROVINCE_COLUMN: 'provincia'}

    def rowCount(self, model_index=QModelIndex()):
        return len(self.patients)

    def columnCount(self, model_index=QModelIndex()):
        return len(self._index_to_field_name)

    def data(self, model_index=QModelIndex(), role=Qt.DisplayRole):
        if role == Qt.DisplayRole and model_index.isValid():
            patient = self.patients[model_index.row()]
            col = model_index.column()

            if col != PROVINCE_COLUMN:
                return getattr(patient, self._index_to_field_name[col])
            return patient.provincia.nombre

        if role == Qt.UserRole:
            return self.patients[model_index.row()].id

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._index_to_field_name[section].capitalize()
        return None

    def sort(self, column, order=Qt.AscendingOrder):
        column_name = self._index_to_field_name[column]
        reverse = order == Qt.DescendingOrder

        self.layoutAboutToBeChanged.emit()

        if column != PROVINCE_COLUMN:
            self.patients.sort(key=lambda p: getattr(p, column_name),
                               reverse=reverse)
        else:
            self.patients.sort(key=lambda p: p.provincia.nombre,
                               reverse=reverse)

        ifrom = self.createIndex(0, 0)
        ito = self.createIndex(len(self.patients), len(self._index_to_field_name))

        self.changePersistentIndex(ifrom, ito)
        self.layoutChanged.emit()
