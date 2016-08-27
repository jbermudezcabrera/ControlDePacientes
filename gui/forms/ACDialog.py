import os

from PyQt4 import uic

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QDialogButtonBox

__author__ = 'Juan Manuel Bermúdez Cabrera'


class ACDialog(QDialog):
    def __init__(self, *args):
        super(ACDialog, self).__init__(*args)

        uic.loadUi(os.path.join('resources', 'uis', 'ACDialog.ui'), self)

        self.buttonBox.button(QDialogButtonBox.Save).setText('Guardar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

        self.buttonBox.accepted.connect(self.on_save)

        self.hb = None
        self.gli = None
        self.crea = None
        self.col = None
        self.trig = None
        self.au = None

        self._data_collected = False

    def modify_ac(self, ac):
        if ac is not None:
            self.hbInput.setValue(ac.hb)
            self.gliInput.setValue(ac.glicemia)
            self.creaInput.setValue(ac.creatinina)
            self.colInput.setValue(ac.colesterol)
            self.trigInput.setValue(ac.trigliceridos)
            self.acidInput.setValue(ac.acido_urico)

    @property
    def data_collected(self):
        return self._data_collected

    @pyqtSlot()
    def on_save(self):
        self.hb = self.hbInput.value()
        self.gli = self.gliInput.value()
        self.crea = self.creaInput.value()
        self.col = self.colInput.value()
        self.trig = self.trigInput.value()
        self.au = self.acidInput.value()

        self._data_collected = True
        self.close()
